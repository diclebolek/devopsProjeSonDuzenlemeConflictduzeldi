'use client';
import { usePathname } from 'next/navigation';
import Header from './Header';

export default function HeaderWrapper() {
  const pathname = usePathname();
  const isAuthPage = pathname === '/login' || pathname === '/register';
  if (isAuthPage) return null;
  return <Header variant="dark" />;
}
