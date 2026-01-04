import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import BookChatbot from '@site/src/components/BookChatbot/BookChatbot';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useLocation } from '@docusaurus/router';
import clsx from 'clsx';
import './Layout.css';

import type { Props } from '@theme/DocItem/Layout';

export default function DocItemLayout({ children }: Props): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  const location = useLocation();
  const [selectedText, setSelectedText] = useState('');

  useEffect(() => {
    const handleSelectionChange = () => {
      const text = window.getSelection()?.toString().trim() || '';
      setSelectedText(text);
    };

    document.addEventListener('selectionchange', handleSelectionChange);
    return () => {
      document.removeEventListener('selectionchange', handleSelectionChange);
    };
  }, []);

  return (
    <Layout wrapperClassName="doc-page-wrapper">
      <div className="container margin-vert--lg">
        <div className="row">
          {/* Book Content Column */}
          <div className={clsx('col', { 'col--7': location.pathname.startsWith('/docs') })}>
            <main className="doc-markdown">
              {children}
              {selectedText && (
                <div className="text-selection-indicator">
                  Selected: "{selectedText.substring(0, 50)}{selectedText.length > 50 ? '...' : ''}"
                </div>
              )}
            </main>
          </div>

          {/* Chatbot Column - Only show on documentation pages */}
          {location.pathname.startsWith('/docs') && (
            <div className="col col--5">
              <div className="chatbot-sidebar">
                <BookChatbot />
              </div>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
}