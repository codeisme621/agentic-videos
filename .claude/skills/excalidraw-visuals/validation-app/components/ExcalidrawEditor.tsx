'use client';

import { useEffect, useState } from 'react';
import "@excalidraw/excalidraw/index.css";

export default function ExcalidrawEditor() {
  const [Excalidraw, setExcalidraw] = useState<any>(null);
  const [convertToExcalidrawElements, setConvertToExcalidrawElements] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [loadStatus, setLoadStatus] = useState<string>('');
  const [excalidrawAPI, setExcalidrawAPI] = useState<any>(null);

  useEffect(() => {
    // Dynamically import Excalidraw for client-side rendering
    import('@excalidraw/excalidraw').then((module) => {
      setExcalidraw(() => module.Excalidraw);
      setConvertToExcalidrawElements(() => module.convertToExcalidrawElements);
      setIsLoading(false);
    });
  }, []);

  // Auto-load file from public/excalidraw/ when component and API are ready
  useEffect(() => {
    if (!isLoading && Excalidraw && excalidrawAPI) {
      loadExcalidrawFile();
    }
  }, [isLoading, Excalidraw, excalidrawAPI]);

  const loadExcalidrawFile = async () => {
    try {
      setLoadStatus('🔍 Looking for .excalidraw files...');
      const response = await fetch('/api/load-excalidraw');
      const data = await response.json();

      if (!response.ok) {
        if (response.status === 404) {
          setLoadStatus('📂 No .excalidraw files found. Use copy_to_validation.py to add files.');
          setTimeout(() => setLoadStatus(''), 5000);
          return;
        }
        throw new Error(data.error || 'Failed to load file');
      }

      // Update the Excalidraw scene using the API
      const sceneData = {
        elements: data.elements,
        appState: {
          ...data.appState,
          viewBackgroundColor: data.appState?.viewBackgroundColor || "#ffffff",
          gridSize: data.appState?.gridSize || null,
          theme: data.appState?.theme || "light"
        }
      };

      excalidrawAPI.updateScene(sceneData);
      setLoadStatus(`✅ Loaded ${data.fileName} (${data.visibleElements}/${data.totalElements} visible elements)`);

      // Auto-fit content to viewport after a short delay
      setTimeout(() => {
        if (excalidrawAPI) {
          excalidrawAPI.scrollToContent();
        }
      }, 500);

      setTimeout(() => setLoadStatus(''), 3000);
    } catch (error) {
      console.error('Error loading file:', error);
      setLoadStatus(`❌ Error: ${error instanceof Error ? error.message : 'Failed to load'}`);
      setTimeout(() => setLoadStatus(''), 5000);
    }
  };

  if (isLoading || !Excalidraw) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <div className="text-lg text-gray-600">Loading Excalidraw...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full h-screen relative">
      {/* Status Panel */}
      {loadStatus && (
        <div className="absolute top-4 left-4 bg-white shadow-lg rounded-lg p-3 max-w-sm z-50">
          <div className={`p-2 rounded text-xs ${
            loadStatus.startsWith('❌') ? 'bg-red-100 text-red-800' :
            loadStatus.startsWith('✅') ? 'bg-green-100 text-green-800' :
            loadStatus.startsWith('📂') ? 'bg-yellow-100 text-yellow-800' :
            'bg-blue-100 text-blue-800'
          }`}>
            {loadStatus}
          </div>
        </div>
      )}

      {/* Reload Button */}
      <div className="absolute top-4 right-4 bg-white shadow-lg rounded-lg p-2 z-50">
        <button
          onClick={loadExcalidrawFile}
          className="px-3 py-2 bg-gray-600 text-white text-xs rounded hover:bg-gray-700"
          title="Reload .excalidraw file"
        >
          🔄 Reload
        </button>
      </div>

      <Excalidraw
        excalidrawAPI={(api) => setExcalidrawAPI(api)}
        onChange={(elements, appState) => {
          // Handle changes if needed - could save state here
        }}
        onPointerUpdate={(payload) => {
          // Handle pointer updates if needed
        }}
      />
    </div>
  );
}