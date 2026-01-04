import { useState, useEffect } from 'react';

const useSelection = (): [string, () => void] => {
  const [selectedText, setSelectedText] = useState('');

  const getSelectedText = () => {
    const text = window.getSelection()?.toString().trim() || '';
    setSelectedText(text);
    return text;
  };

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

  return [selectedText, getSelectedText];
};

export default useSelection;