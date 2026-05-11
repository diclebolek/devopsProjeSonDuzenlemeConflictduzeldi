import Link from 'next/link';
import PageBanner from '@/components/PageBanner';
import { apiService } from '@/lib/api';

async function getBlog(slug: string) {
  try {
    const res = await apiService.getBlogBySlug(slug);
    return res.data;
  } catch { return null; }
}

const recentPosts = [
  { img: '/assets/img/blog-sidebar-thumb-1.png', title: 'Aliquam eros justo, posuere loborti viverra', date: 'Oct 19, 2022' },
  { img: '/assets/img/blog-sidebar-thumb-2.png', title: 'Aliquam eros justo, posuere loborti viverra', date: 'Oct 20, 2022' },
  { img: '/assets/img/blog-sidebar-thumb-1.png', title: 'Aliquam eros justo, posuere loborti viverra', date: 'Oct 21, 2022' },
];
const tags = ['Insurance', 'Life Insurance', 'Health', 'Property', 'Auto', 'Business', 'Cyber', 'Claims'];

export default async function BlogDetailPage({ params }: { params: { slug: string } }) {
  const blog = await getBlog(params.slug);
  const title = blog?.title || 'Giving You the Power to Protect Your Loved Ones and Secure Your Financial Future';
  const content = blog?.content || 'Aliquam eros posuere loborti viverra laoree ullamcorper posuere viverra eros justo, posuere lobo viverra laoreet augue mattis fermentum ullamcorper viverra. Aliquam eros justo, posuere loborti viverra laoreet matti ullamcorper posuere viverra. Aliquam eros justo, posuere lobortis non, viverra laoreet augue mattis fermentum ullamcorper viverra.';
  const img = blog?.cover_image_url || '/assets/img/blog-details.png';
  const author = blog?.author || 'Admin';
  const date = blog?.published_at ? new Date(blog.published_at).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }) : 'October 19, 2022';
  const category = blog?.category ? (typeof blog.category === 'object' ? blog.category.name : blog.category) : 'Insurance';

  return (
    <>
      <PageBanner title="Blog Details" breadcrumb="Blog Details" />
      <div className="lg:pt-[120px] lg:pb-[240px] pt-[60px] pb-[120px]">
        <div className="theme-container mx-auto">
          <div className="lg:grid grid-cols-12 lg:gap-[30px]">
            {/* Main Content */}
            <div className="body-content-wrapper lg:col-span-8 col-span-12 mb-[80px] lg:mb-0">
              <div className="pb-[60px] border-b border-primaryBorder">
                <p className="sm:text-[30px] font-semibold spline-sans sm:leading-9 text-2xl text-primary-900 mb-2">{title}</p>
                <ul className="flex space-x-5 items-center mb-[30px]">
                  <li><span className="text-base leading-[27px] text-primary-100">By {author}</span></li>
                  <li className="flex space-x-2 items-center">
                    <div className="w-2.5 h-2.5 rounded-full bg-primary-500"></div>
                    <span className="text-base leading-[27px] text-primary-100">{category}</span>
                  </li>
                  <li className="flex space-x-2 items-center">
                    <div className="w-2.5 h-2.5 rounded-full bg-primary-500"></div>
                    <span className="text-base leading-[27px] text-primary-100">{date}</span>
                  </li>
                </ul>
                <div className="w-full h-[438px] mb-[30px] overflow-hidden rounded">
                  <img src={img} alt={title} className="w-full h-full object-cover" />
                </div>
                <p className="text-base leading-[27px] text-primary-100 mb-2.5">{content}</p>
                <p className="text-base leading-[27px] text-primary-100 mb-[60px]">Aliquam eros justo, posuere loborti viverra laoreet matti ullamcorper posuere viverra. Aliquam eros justo, posuere lobortis non, viverra laoreet augue mattis fermentum ullamcorper viverra laoreet.</p>
                <div className="sm:flex sm:space-x-[30px] mb-5">
                  <div className="sm:w-2/3 mb-5 sm:mb-0">
                    <img src="/assets/img/blog-details-2.png" alt="" className="w-full h-[380px] object-cover" />
                  </div>
                  <div className="sm:w-1/3 flex flex-col space-y-[30px]">
                    <img src="/assets/img/blog-details-3.png" alt="" className="w-full h-[175px] object-cover" />
                    <img src="/assets/img/blog-details-4.png" alt="" className="w-full h-[175px] object-cover" />
                  </div>
                </div>
                <p className="text-base leading-[27px] text-primary-100 mb-10">Aliquam eros posuere loborti viverra laoree ullamcorper posuere viverra eros justo, posuere lobo viverra laoreet augue mattis fermentum ullamcorper viverra.</p>
                <div className="flex space-x-[15px] mb-5">
                  <div className="w-1/2">
                    <p className="text-lg text-gray-700 spline-sans font-semibold leading-[27px]">Covering You When You Need it Most Trust Us to Keep You Covered</p>
                  </div>
                  <div className="w-1/2">
                    <p className="text-base leading-[27px] text-primary-100">Aliquam eros justo, posuere loborti viverra laoreematti ullamcorper posuere viverra .Aliquam eros just.</p>
                  </div>
                </div>
                <p className="text-base leading-[27px] text-primary-100 mb-[80px]">Aliquam eros justo, posuere loborti viverra laoreet matti ullamcorper posuere viverra .Aliquam eros justo, posuere lobortis, viverra laoreet augue mattis fermentum ullamcorper viverra laoreet.</p>
                {/* Author card */}
                <div className="w-full sm:h-[180px] p-5 sm:p-0 border border-primaryBorder rounded sm:flex items-center sm:space-x-[30px] mb-[30px]">
                  <div className="w-[180px] h-full mb-5 sm:mb-0 overflow-hidden">
                    <img src="/assets/img/blog-details-person.png" alt="Author" className="w-full h-full object-cover" />
                  </div>
                  <div className="flex-1 pr-5">
                    <p className="text-lg text-gray-700 spline-sans font-semibold leading-[27px] mb-2.5">Stanio lainto</p>
                    <p className="text-base leading-[27px] text-gray-700">Ished fact that a reader will be distrol acted bioii the. ished fact th reader will be distrol ac laoreet Aliquam fact that a reader will be distrol acted.</p>
                  </div>
                </div>
                {/* Social Share */}
                <div className="flex space-x-2.5 items-center">
                  <span className="text-lg spline-sans font-bold leading-7 text-primary-900">Share:</span>
                  {['facebook', 'twitter', 'instagram'].map((s) => (
                    <a key={s} href="#" className="w-[50px] h-[50px] rounded flex justify-center items-center text-primary-900 bg-primary-50 hover:text-white hover:bg-primary-900 common-trans">
                      <span className="text-sm font-bold">{s[0].toUpperCase()}</span>
                    </a>
                  ))}
                </div>
              </div>

              {/* Prev / Next */}
              <div className="flex justify-between items-center py-10 border-b border-primaryBorder mb-[60px]">
                <div className="flex space-x-[30px] items-center">
                  <Link href="/blog">
                    <div className="w-[60px] h-[60px] rounded-full bg-primary-50 text-primary-500 hover:bg-primary-500 hover:text-white common-trans flex justify-center items-center">
                      <svg width="15" height="13" viewBox="0 0 15 13" fill="none" xmlns="http://www.w3.org/2000/svg" className="fill-current">
                        <path d="M14.9688 7C14.9688 7.5625 14.5312 8 14 8H4.40625L7.6875 11.3125C8.09375 11.6875 8.09375 12.3438 7.6875 12.7188C7.5 12.9062 7.25 13 7 13C6.71875 13 6.46875 12.9062 6.28125 12.7188L1.28125 7.71875C0.875 7.34375 0.875 6.6875 1.28125 6.3125L6.28125 1.3125C6.65625 0.90625 7.3125 0.90625 7.6875 1.3125C8.09375 1.6875 8.09375 2.34375 7.6875 2.71875L4.40625 6H14C14.5312 6 14.9688 6.46875 14.9688 7Z" />
                      </svg>
                    </div>
                  </Link>
                  <div className="sm:block hidden">
                    <p className="text-base text-primary-100 mb-1.5">Previous post</p>
                    <p className="text-lg text-primary-900 spline-sans font-semibold">Insure your peace of mind</p>
                  </div>
                </div>
                <div className="flex space-x-[30px] items-center">
                  <div className="sm:block hidden">
                    <p className="text-base text-primary-100 mb-1.5 text-end">Next post</p>
                    <p className="text-lg text-primary-900 spline-sans font-semibold text-end">Insure your peace of mind</p>
                  </div>
                  <Link href="/blog">
                    <div className="w-[60px] h-[60px] rounded-full bg-primary-50 text-primary-500 hover:bg-primary-500 hover:text-white common-trans flex justify-center items-center">
                      <svg width="15" height="13" viewBox="0 0 15 13" fill="none" xmlns="http://www.w3.org/2000/svg" className="fill-current">
                        <path d="M0.03125 6C0.03125 5.4375 0.46875 5 1 5L10.5938 5L7.3125 1.6875C6.90625 1.3125 6.90625 0.65625 7.3125 0.28125C7.5 0.09375 7.75 0 8 0C8.28125 0 8.53125 0.09375 8.71875 0.28125L13.7188 5.28125C14.125 5.65625 14.125 6.3125 13.7188 6.6875L8.71875 11.6875C8.34375 12.0938 7.6875 12.0938 7.3125 11.6875C6.90625 11.3125 6.90625 10.6562 7.3125 10.2812L10.5938 7L1 7C0.46875 7 0.03125 6.53125 0.03125 6Z" />
                      </svg>
                    </div>
                  </Link>
                </div>
              </div>

              {/* Comment form */}
              <p className="sm:text-[30px] font-semibold spline-sans sm:leading-9 text-2xl text-primary-900 mb-2">Leave a comment</p>
              <p className="sm:text-base sm:leading-[27px] text-sm text-primary-100 mb-10">By using this form you agree with the message storage, you can contact us directly now.</p>
              <div className="sm:grid grid-cols-2 gap-[30px] mb-[30px]">
                <div className="flex flex-col space-y-5 mb-5 sm:mb-0">
                  <input type="text" placeholder="Your Name" className="w-full h-[68px] rounded border border-primaryBorder focus:outline-none focus:ring-0 px-5 placeholder:text-primary-100 text-black" />
                  <input type="email" placeholder="E-mail" className="w-full h-[68px] rounded border border-primaryBorder focus:outline-none focus:ring-0 px-5 placeholder:text-primary-100 text-black" />
                  <input type="text" placeholder="Phone Number" className="w-full h-[68px] rounded border border-primaryBorder focus:outline-none focus:ring-0 px-5 placeholder:text-primary-100 text-black" />
                </div>
                <textarea placeholder="Write your message" className="w-full h-full rounded border border-primaryBorder focus:outline-none focus:ring-0 p-5 placeholder:text-primary-100 text-black min-h-[200px]"></textarea>
              </div>
              <div className="mb-[60px]">
                <button className="rounded border border-primaryBorder hover:border-transparent hover:bg-primary-500 common-trans group w-full sm:h-[68px] h-[50px] text-black flex justify-center items-center">
                  <span className="sm:text-lg text-sm font-semibold spline-sans text-gray-800 group-hover:text-white common-trans">Submit Now</span>
                </button>
              </div>
            </div>

            {/* Sidebar */}
            <aside className="aside-wrapper lg:col-span-4 col-span-12">
              {/* Search */}
              <div className="w-full mb-[30px]">
                <div className="search-bar w-full h-[50px] bg-secondary rounded flex justify-between items-center overflow-hidden">
                  <input type="text" placeholder="Search Blogs . . ." className="flex-1 h-full focus:outline-none focus:ring-0 px-5 bg-transparent placeholder:text-primary-100 text-black text-sm" />
                  <button className="w-[50px] h-full bg-primary-500 hover:bg-primary-900 common-trans flex justify-center items-center flex-shrink-0">
                    <svg width="18" height="18" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M16.25 8.625C16.25 10.4219 15.6641 12.1016 14.6875 13.4297L19.6094 18.3906C20.1172 18.8594 20.1172 19.6797 19.6094 20.1484C19.1406 20.6562 18.3203 20.6562 17.8516 20.1484L12.8906 15.1875C11.5625 16.2031 9.88281 16.75 8.125 16.75C3.63281 16.75 0 13.1172 0 8.625C0 4.17188 3.63281 0.5 8.125 0.5C12.5781 0.5 16.25 4.17188 16.25 8.625ZM8.125 14.25C11.2109 14.25 13.75 11.75 13.75 8.625C13.75 5.53906 11.2109 3 8.125 3C5 3 2.5 5.53906 2.5 8.625C2.5 11.75 5 14.25 8.125 14.25Z" fill="white" />
                    </svg>
                  </button>
                </div>
              </div>
              {/* Recent Posts */}
              <div className="w-full mb-[30px]">
                <p className="text-lg leading-7 spline-sans font-bold text-primary-900 mb-[30px]">Recent Post</p>
                <div className="flex flex-col space-y-5">
                  {recentPosts.map((p, i) => (
                    <div key={i} className="flex space-x-[15px] items-center">
                      <div className="w-[80px] h-[80px] rounded overflow-hidden flex-shrink-0">
                        <img src={p.img} alt={p.title} className="w-full h-full object-cover" />
                      </div>
                      <div>
                        <Link href="/blog">
                          <p className="text-sm font-semibold spline-sans text-primary-900 hover:text-primary-500 common-trans leading-5 mb-1">{p.title}</p>
                        </Link>
                        <p className="text-xs text-primary-100">{p.date}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
              {/* Tags */}
              <div className="w-full mb-[30px]">
                <p className="text-lg leading-7 spline-sans font-bold text-primary-900 mb-[30px]">Tags</p>
                <div className="flex flex-wrap gap-2.5">
                  {tags.map((tag) => (
                    <a key={tag} href="#" className="px-4 py-2 border border-primaryBorder rounded text-sm text-primary-100 hover:bg-primary-500 hover:text-white hover:border-primary-500 common-trans">{tag}</a>
                  ))}
                </div>
              </div>
            </aside>
          </div>
        </div>
      </div>
    </>
  );
}
