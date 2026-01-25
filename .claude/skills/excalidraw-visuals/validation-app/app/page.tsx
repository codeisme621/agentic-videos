'use client';

import dynamic from 'next/dynamic';

// Dynamic import to avoid SSR issues with Excalidraw
const ExcalidrawEditor = dynamic(
  () => import('../components/ExcalidrawEditor'),
  {
    ssr: false,
    loading: () => <div className="flex items-center justify-center h-screen text-lg">Loading Excalidraw Editor...</div>
  }
);

export default function Home() {
  return (
    <main className="w-full h-screen">
      <ExcalidrawEditor />
    </main>
  );
}