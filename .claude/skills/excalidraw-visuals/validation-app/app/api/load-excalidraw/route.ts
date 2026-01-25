import { NextResponse } from 'next/server';
import { readdir, readFile } from 'fs/promises';
import { join } from 'path';

export async function GET() {
  try {
    const excalidrawDir = join(process.cwd(), 'public', 'excalidraw');

    // Check if directory exists and list files
    let files: string[] = [];
    try {
      const dirContents = await readdir(excalidrawDir);
      files = dirContents.filter(file => file.endsWith('.excalidraw'));
    } catch (error) {
      // Directory doesn't exist or is empty
      return NextResponse.json({
        error: 'No excalidraw directory found or no .excalidraw files available',
        files: []
      }, { status: 404 });
    }

    if (files.length === 0) {
      return NextResponse.json({
        error: 'No .excalidraw files found in /public/excalidraw/',
        files: []
      }, { status: 404 });
    }

    // Load the first .excalidraw file found
    const fileName = files[0];
    const filePath = join(excalidrawDir, fileName);

    try {
      const fileContent = await readFile(filePath, 'utf-8');
      const data = JSON.parse(fileContent);

      // Validate basic structure
      if (!data.elements || !Array.isArray(data.elements)) {
        return NextResponse.json({
          error: `Invalid .excalidraw file structure in ${fileName}`
        }, { status: 400 });
      }

      // Filter out deleted elements
      const visibleElements = data.elements.filter((element: any) => !element.isDeleted);

      const responseData = {
        fileName,
        totalElements: data.elements.length,
        visibleElements: visibleElements.length,
        availableFiles: files,
        elements: visibleElements,
        appState: {
          ...data.appState,
          viewBackgroundColor: data.appState?.viewBackgroundColor || "#ffffff",
          gridSize: data.appState?.gridSize || null,
          theme: data.appState?.theme || "light"
        }
      };

      return NextResponse.json(responseData);

    } catch (parseError) {
      return NextResponse.json({
        error: `Failed to parse ${fileName}: ${parseError instanceof Error ? parseError.message : 'Invalid JSON'}`,
        files
      }, { status: 400 });
    }

  } catch (error) {
    console.error('Error loading excalidraw file:', error);
    return NextResponse.json({
      error: 'Internal server error loading excalidraw file'
    }, { status: 500 });
  }
}