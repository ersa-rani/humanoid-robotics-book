import React, { useState } from 'react';
import ChatWindow from './ChatWindow';
import ChatInput from './ChatInput';
import useSelection from './useSelection';
import './BookChatbot.css';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

const BookChatbot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, getSelectedText] = useSelection();

  const handleSendMessage = async (content: string, contextText?: string) => {
    // Add user message to the chat
    const userMessage: Message = {
      id: Date.now().toString(),
      content: contextText ? `${content} (with selected text: "${contextText}")` : content,
      role: 'user',
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      // Determine which API endpoint to call based on whether there's selected text
      let response;
      if (contextText) {
        // Call the query-selected endpoint with selected text context
        response = await fetch('http://localhost:8000/v1/query-selected', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            query: { content },
            selectedText: contextText
          }),
        });
      } else {
        // Call the regular query endpoint
        response = await fetch('http://localhost:8000/v1/query', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ content }),
        });
      }

      if (response.ok) {
  const data = await response.json();
  console.log("Backend response:", data);

  const assistantMessage: Message = {
    id: Date.now().toString(),
    content: data.answer || data.response || data.content || "No reply from assistant",
    role: 'assistant',
    timestamp: new Date(),
  };

  setMessages((prev) => [...prev, assistantMessage]);
}
 else {
        // Handle error response
        const errorMessage: Message = {
          id: Date.now().toString(),
          content: 'Sorry, I encountered an error processing your request.',
          role: 'assistant',
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMessage]);
      }
    } catch (error) {
      // Handle network or other errors
      const errorMessage: Message = {
        id: Date.now().toString(),
        content: 'Sorry, I encountered a network error. Please try again.',
        role: 'assistant',
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // Enhanced send message handler that includes selected text if available
  const handleSendMessageWithContext = (content: string) => {
    const currentSelection = getSelectedText();
    handleSendMessage(content, currentSelection || undefined);
  };

  return (
    <div className="book-chatbot-container">
      <div className="chat-window-container">
        <ChatWindow messages={messages} isLoading={isLoading} />
        <ChatInput onSendMessage={handleSendMessageWithContext} isLoading={isLoading} />
      </div>
    </div>
  );
};

export default BookChatbot;