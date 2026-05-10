'use client';
import Link from 'next/link';

interface HeaderProps {
  variant?: 'light' | 'dark';
}

export default function Header({ variant = 'dark' }: HeaderProps) {
  const isLight = variant === 'light';
  const topBarBg = isLight ? 'bg-white border-b border-primaryBorder' : 'bg-[#028835]';
  const topBarText = isLight ? 'text-primary-100' : 'text-white';
  const topBarIconFill = isLight ? '#028835' : 'white';
  const topBarSocialText = isLight ? 'text-gray-800' : 'text-white';

  const navBg = isLight ? 'bg-white border-b border-primaryBorder' : 'bg-primary-900';
  const navText = isLight ? 'text-primary-900' : 'text-white';
  const searchFill = isLight ? '#004C3F' : 'white';
  const logoStyle = isLight ? {} : { filter: 'brightness(0) invert(1)' };

  const dropdownArrow = (
    <span><svg width="7" height="5" viewBox="0 0 7 5" fill="none" xmlns="http://www.w3.org/2000/svg" className="fill-current"><path d="M3.1377 3.85938L0.637695 1.35938C0.43457 1.17188 0.43457 0.84375 0.637695 0.65625C0.825195 0.453125 1.15332 0.453125 1.34082 0.65625L3.49707 2.79688L5.6377 0.65625C5.8252 0.453125 6.15332 0.453125 6.34082 0.65625C6.54395 0.84375 6.54395 1.17188 6.34082 1.35938L3.84082 3.85938C3.65332 4.0625 3.3252 4.0625 3.1377 3.85938Z" /></svg></span>
  );

  return (
    <>
    <header className="fixed top-0 z-[9999] w-full">
      {/* Top Bar */}
      <div className={`top-bar lg:block hidden w-full h-[50px] ${topBarBg}`}>
        <div className="theme-container mx-auto w-full h-full flex justify-between items-center">
          <div className="flex space-x-6 items-center h-full">
            {/* Email */}
            <div className="flex items-center space-x-2">
              <span>
                <svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.5 0C15.2969 0 16 0.703125 16 1.5C16 2 15.75 2.4375 15.375 2.71875L8.59375 7.8125C8.21875 8.09375 7.75 8.09375 7.375 7.8125L0.59375 2.71875C0.21875 2.4375 0 2 0 1.5C0 0.703125 0.65625 0 1.5 0H14.5ZM6.78125 8.625C7.5 9.15625 8.46875 9.15625 9.1875 8.625L16 3.5V10C16 11.125 15.0938 12 14 12H2C0.875 12 0 11.125 0 10V3.5L6.78125 8.625Z" fill={topBarIconFill} />
                </svg>
              </span>
              <p className={`text-sm ${topBarText}`}>info@example.com</p>
            </div>
            {/* Address */}
            <div className="flex items-center space-x-2">
              <span>
                <svg width="12" height="17" viewBox="0 0 12 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M6.71875 15.625C6.34375 16.0938 5.625 16.0938 5.25 15.625C3.65625 13.5938 0 8.75 0 6C0 2.6875 2.6875 0 6 0C9.3125 0 12 2.6875 12 6C12 8.75 8.34375 13.5938 6.71875 15.625ZM6 8C7.09375 8 8 7.125 8 6C8 4.90625 7.09375 4 6 4C4.875 4 4 4.90625 4 6C4 7.125 4.875 8 6 8Z" fill={topBarIconFill} />
                </svg>
              </span>
              <p className={`text-sm ${topBarText}`}>6391 Elgin St. Celina, 10299</p>
            </div>
            {/* Phone */}
            <div className="flex items-center space-x-2">
              <span>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.1719 11.8125L14.4375 14.8125C14.3438 15.3125 13.9062 15.6562 13.4062 15.6562C6 15.625 0 9.625 0 2.21875C0 1.71875 0.3125 1.28125 0.8125 1.1875L3.8125 0.46875C4.28125 0.375 4.78125 0.625 4.96875 1.0625L6.40625 4.25C6.5625 4.65625 6.46875 5.125 6.125 5.40625L4.6875 6.71875C5.71875 8.78125 7.40625 10.4688 9.46875 11.5L10.7812 10.0625C11.0625 9.75 11.5312 9.625 11.9375 9.78125L15.125 11.2188C15.5625 11.4375 15.8125 11.9375 15.1719 11.8125Z" fill={topBarIconFill} />
                </svg>
              </span>
              <p className={`text-sm ${topBarText}`}>(629) 555-0129</p>
            </div>
          </div>
          {/* Social Icons */}
          <div className="flex items-center space-x-4 h-full">
            {[
              { href: 'https://www.facebook.com/', d: 'M8.17383 9.3125H5.97656V15.875H3.04688V9.3125H0.644531V6.61719H3.04688V4.53711C3.04688 2.19336 4.45312 0.875 6.5918 0.875C7.61719 0.875 8.70117 1.08008 8.70117 1.08008V3.39453H7.5C6.32812 3.39453 5.97656 4.09766 5.97656 4.85938V6.61719H8.58398L8.17383 9.3125Z', vb: '0 0 9 16' },
              { href: 'https://www.instagram.com/', d: 'M7.5625 4.00586C9.4082 4.00586 10.9316 5.5293 10.9316 7.375C10.9316 9.25 9.4082 10.7441 7.5625 10.7441C5.6875 10.7441 4.19336 9.25 4.19336 7.375C4.19336 5.5293 5.6875 4.00586 7.5625 4.00586ZM7.5625 9.57227C8.76367 9.57227 9.73047 8.60547 9.73047 7.375C9.73047 6.17383 8.76367 5.20703 7.5625 5.20703C6.33203 5.20703 5.36523 6.17383 5.36523 7.375C5.36523 8.60547 6.36133 9.57227 7.5625 9.57227ZM11.8398 3.88867C11.8398 3.44922 11.4883 3.09766 11.0488 3.09766C10.6094 3.09766 10.2578 3.44922 10.2578 3.88867C10.2578 4.32812 10.6094 4.67969 11.0488 4.67969C11.4883 4.67969 11.8398 4.32812 11.8398 3.88867ZM14.0664 4.67969C14.125 5.76367 14.125 9.01562 14.0664 10.0996C14.0078 11.1543 13.7734 12.0625 13.0117 12.8535C12.25 13.6152 11.3125 13.8496 10.2578 13.9082C9.17383 13.9668 5.92188 13.9668 4.83789 13.9082C3.7832 13.8496 2.875 13.6152 2.08398 12.8535C1.32227 12.0625 1.08789 11.1543 1.0293 10.0996C0.970703 9.01562 0.970703 5.76367 1.0293 4.67969C1.08789 3.625 1.32227 2.6875 2.08398 1.92578C2.875 1.16406 3.7832 0.929688 4.83789 0.871094C5.92188 0.8125 9.17383 0.8125 10.2578 0.871094C11.3125 0.929688 12.25 1.16406 13.0117 1.92578C13.7734 2.6875 14.0078 3.625 14.0664 4.67969ZM12.6602 11.2422C13.0117 10.3926 12.9238 8.3418 12.9238 7.375C12.9238 6.4375 13.0117 4.38672 12.6602 3.50781C12.4258 2.95117 11.9863 2.48242 11.4297 2.27734C10.5508 1.92578 8.5 2.01367 7.5625 2.01367C6.5957 2.01367 4.54492 1.92578 3.69531 2.27734C3.10938 2.51172 2.66992 2.95117 2.43555 3.50781C2.08398 4.38672 2.17188 6.4375 2.17188 7.375C2.17188 8.3418 2.08398 10.3926 2.43555 11.2422C2.66992 11.8281 3.10938 12.2676 3.69531 12.502C4.54492 12.8535 6.5957 12.7656 7.5625 12.7656C8.5 12.7656 10.5508 12.8535 11.4297 12.502C11.9863 12.2676 12.4551 11.8281 12.6602 11.2422Z', vb: '0 0 15 14' },
              { href: 'https://twitter.com/', d: 'M13.4473 3.32812C13.4473 3.47461 13.4473 3.5918 13.4473 3.73828C13.4473 7.81055 10.3711 12.4688 4.7168 12.4688C2.95898 12.4688 1.34766 11.9707 0 11.0918C0.234375 11.1211 0.46875 11.1504 0.732422 11.1504C2.16797 11.1504 3.48633 10.6523 4.54102 9.83203C3.19336 9.80273 2.05078 8.92383 1.66992 7.69336C1.875 7.72266 2.05078 7.75195 2.25586 7.75195C2.51953 7.75195 2.8125 7.69336 3.04688 7.63477C1.64062 7.3418 0.585938 6.11133 0.585938 4.61719V4.58789C0.996094 4.82227 1.49414 4.93945 1.99219 4.96875C1.14258 4.41211 0.615234 3.47461 0.615234 2.41992C0.615234 1.83398 0.761719 1.30664 1.02539 0.867188C2.54883 2.71289 4.83398 3.94336 7.38281 4.08984C7.32422 3.85547 7.29492 3.62109 7.29492 3.38672C7.29492 1.6875 8.67188 0.310547 10.3711 0.310547C11.25 0.310547 12.041 0.662109 12.627 1.27734C13.3008 1.13086 13.9746 0.867188 14.5605 0.515625C14.3262 1.24805 13.8574 1.83398 13.2129 2.21484C13.8281 2.15625 14.4434 1.98047 14.9707 1.74609C14.5605 2.36133 14.0332 2.88867 13.4473 3.32812Z', vb: '0 0 15 13' },
              { href: 'https://www.linkedin.com/', d: 'M12.1875 0.8125C12.6855 0.8125 13.125 1.25195 13.125 1.7793V13C13.125 13.5273 12.6855 13.9375 12.1875 13.9375H0.908203C0.410156 13.9375 0 13.5273 0 13V1.7793C0 1.25195 0.410156 0.8125 0.908203 0.8125H12.1875ZM3.95508 12.0625V5.82227H2.02148V12.0625H3.95508ZM2.98828 4.94336C3.60352 4.94336 4.10156 4.44531 4.10156 3.83008C4.10156 3.21484 3.60352 2.6875 2.98828 2.6875C2.34375 2.6875 1.8457 3.21484 1.8457 3.83008C1.8457 4.44531 2.34375 4.94336 2.98828 4.94336ZM11.25 12.0625V8.63477C11.25 6.96484 10.8691 5.64648 8.90625 5.64648C7.96875 5.64648 7.32422 6.17383 7.06055 6.67188H7.03125V5.82227H5.18555V12.0625H7.11914V8.98633C7.11914 8.16602 7.26562 7.375 8.29102 7.375C9.28711 7.375 9.28711 8.3125 9.28711 9.01562V12.0625H11.25Z', vb: '0 0 14 14' },
            ].map((s, i) => (
              <a key={i} href={s.href} target="_blank" rel="noreferrer" className={`${topBarSocialText} hover:opacity-75 common-trans`}>
                <svg width="14" height="14" viewBox={s.vb} fill="none" xmlns="http://www.w3.org/2000/svg" className="fill-current"><path d={s.d} /></svg>
              </a>
            ))}
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className={`navigation-wrapper w-full h-[90px] ${navBg}`}>
        <div className="theme-container h-full mx-auto">
          <div className="w-full h-full flex justify-between items-center">
            <div className="h-full flex items-center space-x-[72px]">
              <Link href="/">
                <div className="logo-area w-[180px] h-[55px]">
                  <img src="/assets/img/logo.svg" alt="insucom" className="w-full h-full object-contain" style={logoStyle} />
                </div>
              </Link>
              {/* Desktop Nav */}
              <nav className={`nav-wrapper ${!isLight ? 'nav-wrapper-2' : ''} lg:block hidden h-full`}>
                <ul className="flex space-x-7 items-center h-full">
                  <li className="relative group h-full flex items-center">
                    <Link href="/" className={`${navText} flex items-center space-x-1 h-full`}><span>Home</span>{dropdownArrow}</Link>
                    <ul className="absolute left-0 top-[90px] w-[200px] bg-white shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible group-hover:top-[70px] transition-all duration-300 ease-in-out z-50 rounded-b-lg border-t-2 border-primary-500 text-gray-800 font-medium py-2">
                      <li><Link href="/" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Home One</Link></li>
                      <li><Link href="/home-2" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Home Two</Link></li>
                    </ul>
                  </li>
                  <li className="h-full flex items-center"><Link href="/about" className={`${navText} h-full flex items-center`}><span>About Us</span></Link></li>
                  <li className="relative group h-full flex items-center">
                    <Link href="/services" className={`${navText} flex items-center space-x-1 h-full`}><span>Services</span>{dropdownArrow}</Link>
                    <ul className="absolute left-0 top-[90px] w-[200px] bg-white shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible group-hover:top-[70px] transition-all duration-300 ease-in-out z-50 rounded-b-lg border-t-2 border-primary-500 text-gray-800 font-medium py-2">
                      <li><Link href="/services" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Services</Link></li>
                      <li><Link href="/services/risk-assessment" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Service Details</Link></li>
                    </ul>
                  </li>
                  <li className="relative group h-full flex items-center">
                    <Link href="/projects" className={`${navText} flex items-center space-x-1 h-full`}><span>Projects</span>{dropdownArrow}</Link>
                    <ul className="absolute left-0 top-[90px] w-[200px] bg-white shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible group-hover:top-[70px] transition-all duration-300 ease-in-out z-50 rounded-b-lg border-t-2 border-primary-500 text-gray-800 font-medium py-2">
                      <li><Link href="/projects" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Projects</Link></li>
                      <li><Link href="/projects/coverage-pro" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Project Details</Link></li>
                    </ul>
                  </li>
                  <li className="relative group h-full flex items-center">
                    <Link href="/blog" className={`${navText} flex items-center space-x-1 h-full`}><span>Blogs</span>{dropdownArrow}</Link>
                    <ul className="absolute left-0 top-[90px] w-[200px] bg-white shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible group-hover:top-[70px] transition-all duration-300 ease-in-out z-50 rounded-b-lg border-t-2 border-primary-500 text-gray-800 font-medium py-2">
                      <li><Link href="/blog" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Blogs</Link></li>
                      <li><Link href="/blog" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Blog Details</Link></li>
                    </ul>
                  </li>
                  <li className="relative group h-full flex items-center">
                    <span className={`${navText} flex items-center space-x-1 cursor-pointer h-full`}><span>Pages</span>{dropdownArrow}</span>
                    <ul className="absolute left-0 top-[90px] w-[200px] bg-white shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible group-hover:top-[70px] transition-all duration-300 ease-in-out z-50 rounded-b-lg border-t-2 border-primary-500 text-gray-800 font-medium py-2">
                      <li><Link href="/faq" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">FAQ</Link></li>
                      <li><Link href="/contact" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Support</Link></li>
                      <li><Link href="/projects" className="block px-5 py-2.5 hover:bg-gray-50 hover:text-primary-500">Projects</Link></li>
                    </ul>
                  </li>
                  <li className="h-full flex items-center"><Link href="/contact" className={`${navText} h-full flex items-center`}><span>Contact</span></Link></li>
                </ul>
              </nav>

              {/* Mobile Nav */}
              <nav className="nav-wrapper mobile-nav-wrapper block lg:hidden">
                <div className="mobile-drawer">
                  <div className="mobile-wid w-[310px] bg-white fixed top-0 h-full px-8 pt-10" style={{ zIndex: 99999 }}>
                    <div className="flex justify-center mb-10"><div className="logo-area w-[180px] h-[55px]"><img src="/assets/img/logo.svg" alt="insucom" className="w-full h-full object-contain" /></div></div>
                    <ul className="flex flex-col mb-10">
                      <li><Link href="/"><span>Home</span></Link></li>
                      <li><Link href="/about"><span>About Us</span></Link></li>
                      <li><Link href="/services"><span>Services</span></Link></li>
                      <li><Link href="/projects"><span>Projects</span></Link></li>
                      <li><Link href="/blog"><span>Blogs</span></Link></li>
                      <li><Link href="/faq"><span>FAQ</span></Link></li>
                      <li><Link href="/contact"><span>Contact</span></Link></li>
                      <li><Link href="/projects"><span>Projects</span></Link></li>
                    </ul>
                    <div className="flex items-center justify-center">
                      <div className="flex flex-col">
                        <span className="spline-sans text-sm text-gray-900 font-medium">Requesting A Call:</span>
                        <span className="text-base font-bold text-gray-900">(629) 555-0129</span>
                      </div>
                    </div>
                  </div>
                  <div id="drawer-away" className="drawer-away w-full h-full fixed bg-black bg-opacity-80 z-30 left-0 top-0"></div>
                </div>
              </nav>
            </div>

            <div className="space-x-[52px] items-center xl:flex hidden">
              {/* Search Icon */}
              <div className="search-bar-wrapper relative">
                <button type="button">
                  <span><svg width="21" height="21" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16.25 8.625C16.25 10.4219 15.6641 12.1016 14.6875 13.4297L19.6094 18.3906C20.1172 18.8594 20.1172 19.6797 19.6094 20.1484C19.1406 20.6562 18.3203 20.6562 17.8516 20.1484L12.8906 15.1875C11.5625 16.2031 9.88281 16.75 8.125 16.75C3.63281 16.75 0 13.1172 0 8.625C0 4.17188 3.63281 0.5 8.125 0.5C12.5781 0.5 16.25 4.17188 16.25 8.625ZM8.125 14.25C11.2109 14.25 13.75 11.75 13.75 8.625C13.75 5.53906 11.2109 3 8.125 3C5 3 2.5 5.53906 2.5 8.625C2.5 11.75 5 14.25 8.125 14.25Z" fill={searchFill} /></svg></span>
                </button>
                <div className="search-form w-[400px] p-5 bg-white shadow-2xl absolute -left-[300px] top-[60px] z-30">
                  <form><div className="relative">
                    <input type="search" className="block w-full p-4 pl-10 text-sm border border-gray-300 rounded-lg bg-primary-50 focus:outline-none text-black focus:ring-0" placeholder="Search..." />
                    <button type="submit" className="text-white absolute right-2.5 bottom-2.5 bg-primary-500 hover:bg-primary-900 focus:outline-none focus:ring-0 font-medium rounded-lg text-sm px-4 py-2">Search</button>
                  </div></form>
                </div>
              </div>

              {/* Get A Quote Button */}
              <Link href="/contact" className="px-[30px] py-5 border border-white rounded-lg text-white font-semibold spline-sans flex space-x-2.5 items-center capitalize hover:bg-white hover:text-primary-900 common-trans">
                <span>Get A Quote</span>
                <span><svg width="15" height="14" viewBox="0 0 15 14" fill="none" xmlns="http://www.w3.org/2000/svg" className="fill-current"><path d="M13.6875 7.71875C14.0938 7.34375 14.0938 6.6875 13.6875 6.3125L8.6875 1.3125C8.3125 0.90625 7.65625 0.90625 7.28125 1.3125C6.875 1.6875 6.875 2.34375 7.28125 2.71875L10.5625 6H1C0.4375 6 0 6.46875 0 7C0 7.5625 0.4375 8 1 8H10.5625L7.28125 11.3125C6.875 11.6875 6.875 12.3438 7.28125 12.7188C7.65625 13.125 8.3125 13.125 8.6875 12.7188L13.6875 7.71875Z" /></svg></span>
              </Link>
            </div>

            {/* Mobile hamburger */}
            <button type="button" id="drawer-btn" className="w-[77px] h-full flex lg:hidden xl:hidden justify-center items-center">
              <span className={navText}>
                <svg width="28" height="22" viewBox="0 0 28 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M28 11H0" stroke="currentColor" strokeWidth="2" />
                  <path d="M21 21H0" stroke="currentColor" strokeWidth="2" />
                  <path d="M20 1H0" stroke="currentColor" strokeWidth="2" />
                </svg>
              </span>
            </button>
          </div>
        </div>
      </div>
    </header>
    {/* Spacer to prevent content overlapping hidden by fixed header */}
    <div className="h-[90px] lg:h-[140px] w-full" />
    </>
  );
}
