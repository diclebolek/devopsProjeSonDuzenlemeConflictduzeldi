'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { apiService } from '@/lib/api';
import Link from 'next/link';

export default function RegisterPage() {
  const router = useRouter();
  const [form, setForm] = useState({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    password: ''
  });
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [errorMsg, setErrorMsg] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('loading');
    setErrorMsg('');
    try {
      await apiService.register(form);
      setStatus('success');
      setTimeout(() => {
        router.push('/login');
      }, 1500);
    } catch (err: any) {
      setStatus('error');
      const apiError = err.response?.data;
      if (apiError && typeof apiError === 'object') {
        // Display specific error messages from Django if available
        const firstKey = Object.keys(apiError)[0];
        setErrorMsg(`${firstKey}: ${apiError[firstKey]}`);
      } else {
        setErrorMsg('Kayıt oluşturulurken bir hata oluştu. Lütfen bilgilerinizi kontrol edip tekrar deneyin.');
      }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#FBF7ED] px-6 py-12">
      <div className="w-full max-w-lg bg-white rounded-2xl shadow-xl overflow-hidden border border-[#028835]/10 my-8">
        <div className="p-8">
          {/* Logo & Header */}
          <div className="text-center mb-8">
            <Link href="/" className="inline-block mb-4">
              <span className="text-3xl font-extrabold text-[#004C3F]">Insucom</span>
            </Link>
            <h1 className="text-2xl font-bold text-[#004C3F]">Hesap Oluştur</h1>
            <p className="text-[#677471] text-sm mt-1">Aramıza katılın ve avantajlardan yararlanın</p>
          </div>

          {status === 'success' ? (
            <div className="bg-[#E6F3EB] border border-[#028835]/20 rounded-xl p-6 text-center">
              <div className="w-16 h-16 bg-[#028835]/10 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#028835" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <h3 className="text-lg font-bold text-[#004C3F] mb-2">Kayıt Başarılı!</h3>
              <p className="text-sm text-[#677471]">Hesabınız başarıyla oluşturuldu. Giriş sayfasına yönlendiriliyorsunuz...</p>
            </div>
          ) : (
            <form id="register-form" onSubmit={handleSubmit} className="space-y-5">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-semibold text-[#004C3F] mb-1.5 ml-1">Adınız</label>
                  <input
                    name="first_name"
                    type="text"
                    required
                    value={form.first_name}
                    onChange={handleChange}
                    className="w-full h-11 px-4 rounded-xl border border-gray-200 focus:border-[#028835] focus:ring-2 focus:ring-[#028835]/10 transition-all outline-none text-gray-700 text-sm"
                    placeholder="Adınız"
                  />
                </div>
                <div>
                  <label className="block text-sm font-semibold text-[#004C3F] mb-1.5 ml-1">Soyadınız</label>
                  <input
                    name="last_name"
                    type="text"
                    required
                    value={form.last_name}
                    onChange={handleChange}
                    className="w-full h-11 px-4 rounded-xl border border-gray-200 focus:border-[#028835] focus:ring-2 focus:ring-[#028835]/10 transition-all outline-none text-gray-700 text-sm"
                    placeholder="Soyadınız"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-semibold text-[#004C3F] mb-1.5 ml-1">Kullanıcı Adı</label>
                <input
                  name="username"
                  type="text"
                  required
                  value={form.username}
                  onChange={handleChange}
                  className="w-full h-11 px-4 rounded-xl border border-gray-200 focus:border-[#028835] focus:ring-2 focus:ring-[#028835]/10 transition-all outline-none text-gray-700 text-sm"
                  placeholder="Kullanıcı Adı"
                />
              </div>

              <div>
                <label className="block text-sm font-semibold text-[#004C3F] mb-1.5 ml-1">E-posta Adresi</label>
                <input
                  name="email"
                  type="email"
                  required
                  value={form.email}
                  onChange={handleChange}
                  className="w-full h-11 px-4 rounded-xl border border-gray-200 focus:border-[#028835] focus:ring-2 focus:ring-[#028835]/10 transition-all outline-none text-gray-700 text-sm"
                  placeholder="ornek@mail.com"
                />
              </div>

              <div>
                <label className="block text-sm font-semibold text-[#004C3F] mb-1.5 ml-1">Şifre</label>
                <input
                  name="password"
                  type="password"
                  required
                  minLength={8}
                  value={form.password}
                  onChange={handleChange}
                  className="w-full h-11 px-4 rounded-xl border border-gray-200 focus:border-[#028835] focus:ring-2 focus:ring-[#028835]/10 transition-all outline-none text-gray-700 text-sm"
                  placeholder="En az 8 karakter"
                />
              </div>

              {status === 'error' && (
                <div className="bg-red-50 border border-red-100 text-red-600 rounded-xl px-4 py-3 text-sm flex items-center space-x-2">
                  <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>
                  <span className="capitalize">{errorMsg}</span>
                </div>
              )}

              <button
                id="register-submit"
                type="submit"
                disabled={status === 'loading'}
                style={{ backgroundColor: status === 'loading' ? '#004C3F' : '#028835' }}
                className="w-full h-12 mt-2 text-white font-bold rounded-xl shadow-lg transition-all transform active:scale-[0.98] disabled:opacity-70 disabled:cursor-not-allowed hover:opacity-90"
              >
                {status === 'loading' ? 'Kaydediliyor...' : 'Ücretsiz Kayıt Ol'}
              </button>
            </form>
          )}

          <div className="mt-8 pt-6 border-t border-gray-50 text-center">
            <p className="text-sm text-[#677471]">
              Zaten bir hesabınız var mı?{' '}
              <Link id="login-link" href="/login" className="text-[#028835] font-bold hover:underline">Giriş Yapın</Link>
            </p>
            <Link href="/" className="inline-block mt-4 text-xs text-[#677471] hover:text-[#028835] transition-colors">
              ← Ana Sayfaya Dön
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
