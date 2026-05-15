'use client';
import { useEffect } from 'react';

type SliderType = 'test-two-swiper-wrapper' | 'related-post-slider-wrap' | 'insu-swiper' | 'financ-swiper';

interface ClientSliderProps {
  children: React.ReactNode;
  type: SliderType;
}

export default function ClientSlider({ children, type }: ClientSliderProps) {
  useEffect(() => {
    if (typeof window !== 'undefined' && (window as any).Swiper) {
      const config: any = {
        slidesPerView: 1,
        spaceBetween: 30,
        speed: 2000,
        autoplay: { delay: 3000, disableOnInteraction: false },
        pagination: { el: ".swiper-pagination", clickable: true },
      };

      if (type === 'test-two-swiper-wrapper') {
        config.breakpoints = {
          1024: { slidesPerView: 2 },
          1440: { slidesPerView: 3 },
        };
      } else if (type === 'related-post-slider-wrap') {
        config.navigation = {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        };
        // Remove pagination for related post slider as per original plugins.js line 58
      }

      new (window as any).Swiper(`.${type}`, config);
    }
  }, [type]);

  return <>{children}</>;
}
