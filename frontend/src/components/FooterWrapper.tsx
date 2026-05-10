'use client';
import { usePathname } from 'next/navigation';
import Footer from './Footer';
import FooterTwo from './FooterTwo';

export default function FooterWrapper() {
  const pathname = usePathname();
  // Only standard root homepage gets Footer1 (dark). All internal pages and home-2 get light footer.
  const isHome = pathname === '/';
  
  return isHome ? <Footer /> : <FooterTwo />;
}
