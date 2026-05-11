'use client';
import { usePathname } from 'next/navigation';
import Header from './Header';

export default function HeaderWrapper() {
  const pathname = usePathname();
  const isHome = pathname === '/' || pathname === '/home-2';
  return <Header variant="dark" />;
}
