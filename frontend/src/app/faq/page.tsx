'use client';

import { useState } from 'react';
import PageBanner from '@/components/PageBanner';

const faqs = [
  { q: 'What is a claim?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What are the types of insurance?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What is a premium?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What is a deductible?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'How is the cost of insurance determined?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What is insurance?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What are the main coverage options?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'How to choose the best policy?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'What documents are required?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
  { q: 'Is there any online support?', a: 'Insurance is a contract between an individual or an organization and an insurance company that protects against financial loss or damage' },
];

export default function FaqPage() {
  const [activeIndex, setActiveIndex] = useState<number | null>(0);

  const toggleFaq = (index: number) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  const renderFaqItem = (faq: { q: string; a: string }, index: number) => {
    const isOpen = activeIndex === index;
    return (
      <div key={index} className="faq-item w-full border-b border-primaryBorder">
        <button
          type="button"
          onClick={() => toggleFaq(index)}
          className="faq-btn flex justify-between items-center w-full py-5 text-left"
        >
          <span className="text-lg font-semibold spline-sans leading-[27px] text-primary-900">
            {faq.q}
          </span>
          <span className={`transform transition-transform duration-300 ${isOpen ? 'rotate-180' : ''}`}>
            <svg width="14" height="8" viewBox="0 0 14 8" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M7 8C6.71875 8 6.46875 7.90625 6.28125 7.71875L1.28125 2.71875C0.875 2.34375 0.875 1.6875 1.28125 1.3125C1.65625 0.90625 2.3125 0.90625 2.6875 1.3125L7 5.59375L11.2812 1.3125C11.6562 0.90625 12.3125 0.90625 12.6875 1.3125C13.0938 1.6875 13.0938 2.34375 12.6875 2.71875L7.6875 7.71875C7.5 7.90625 7.25 8 7 8Z"
                fill="#004C3F"
              />
            </svg>
          </span>
        </button>
        <div className={`faq-body overflow-hidden transition-all duration-300 ease-in-out ${isOpen ? 'max-h-[200px]' : 'max-h-0'}`}>
          <p className="text-base leading-7 text-primary-100 mb-5">
            {faq.a}
          </p>
        </div>
      </div>
    );
  };

  return (
    <>
      <PageBanner title="FAQ" breadcrumb="FAQ" />
      <div className="faq-page-wrapper lg:pt-[120px] lg:pb-[240px] pt-[60px] pb-[120px]">
        <div className="theme-container mx-auto">
          <div className="flex justify-center">
            <div>
              <p className="text-primary-500 font-bold sm:leading-8 spline-sans sm:text-xl text-lg uppercase mb-2 text-center">
                Some FAQ’s
              </p>
              <h2 className="headline-default text-primary-900 mb-[60px] text-center">
                Trust us to keep you covered
              </h2>
            </div>
          </div>
          <div className="grid lg:grid-cols-2 grid-cols-1 lg:gap-[30px]">
            {/* Left Column */}
            <div>
              {faqs.slice(0, 5).map((faq, i) => renderFaqItem(faq, i))}
            </div>
            
            {/* Right Column */}
            <div>
              {faqs.slice(5, 10).map((faq, i) => renderFaqItem(faq, i + 5))}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
