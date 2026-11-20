import { lazy, Suspense } from 'react';
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router-dom';
import { AppShell } from './layouts/AppShell';
const HomePage = lazy(() => import('./pages/HomePage').then(module => ({ default: module.HomePage })));
const LessonPage = lazy(() => import('./pages/LessonPage').then(module => ({ default: module.LessonPage })));
const KanjiHubPage = lazy(() => import('./pages/KanjiHubPage').then(module => ({ default: module.KanjiHubPage })));
const ExamPage = lazy(() => import('./pages/ExamPage').then(module => ({ default: module.ExamPage })));
const KaiwaPage = lazy(() => import('./pages/KaiwaPage').then(module => ({ default: module.KaiwaPage })));

const router = createBrowserRouter([
  {
    path: '/',
    element: <AppShell />,
    children: [
      { index: true, element: <HomePage /> },
      { path: 'lessons/:level/:id', element: <LessonPage /> },
      { path: 'kanji', element: <KanjiHubPage /> },
      { path: 'tests', element: <ExamPage /> },
      { path: 'kaiwa', element: <KaiwaPage /> },
      { path: '*', element: <Navigate to="/" replace /> },
    ],
  },
]);

export function App() {
  return <Suspense fallback={<p role="status">Đang tải không gian học…</p>}><RouterProvider router={router} /></Suspense>;
}
