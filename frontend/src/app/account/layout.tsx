'use client';

import Link from 'next/link';
import { useRouter, usePathname } from 'next/navigation';
import { useEffect } from 'react';

const accountLinks = [
  { href: '/account/policies', label: 'Poliçelerim', emoji: '📋' },
  { href: '/account/quotes', label: 'Tekliflerim', emoji: '💼' },
  { href: '/account/claims', label: 'Hasar Kayıtları', emoji: '🔧' },
  { href: '/account/payments', label: 'Ödemelerim', emoji: '💳' },
  { href: '/account/alerts', label: 'Bildirimlerim', emoji: '🔔' },
];

export default function AccountLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const token = localStorage.getItem('access_token');
      if (!token) router.push('/login');
    }
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    router.push('/login');
  };

  return (
    <div className="min-h-screen bg-[#FBF7ED] py-10 px-6 lg:px-10">
      <div className="max-w-7xl mx-auto grid md:grid-cols-4 gap-8">
        {/* Sidebar */}
        <aside className="md:col-span-1">
          <div className="card p-6 sticky top-24">
            <div className="flex items-center gap-3 mb-6 pb-6 border-b border-[#E3E3E3]">
              <div className="w-12 h-12 rounded-full bg-[#E6F3EB] flex items-center justify-center text-2xl">👤</div>
              <div>
                <p className="font-bold text-[#004C3F] text-sm">Hesabım</p>
                <p className="text-xs text-[#677471]">Demo Kullanıcı</p>
              </div>
            </div>
            <nav className="space-y-1">
              {accountLinks.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-colors ${
                    pathname === link.href
                      ? 'bg-[#028835] text-white'
                      : 'text-[#677471] hover:bg-[#E6F3EB] hover:text-[#004C3F]'
                  }`}
                >
                  <span>{link.emoji}</span>
                  {link.label}
                </Link>
              ))}
            </nav>
            <div className="mt-6 pt-6 border-t border-[#E3E3E3]">
              <button
                id="logout-btn"
                onClick={handleLogout}
                className="w-full text-left flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-red-500 hover:bg-red-50 transition-colors"
              >
                <span>🚪</span> Çıkış Yap
              </button>
            </div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="md:col-span-3">{children}</main>
      </div>
    </div>
  );
}
