'use client';

interface SafeImageProps {
  src: string;
  alt: string;
  className?: string;
  fallback?: React.ReactNode;
}

export default function SafeImage({ src, alt, className, fallback }: SafeImageProps) {
  if (!src) return <>{fallback ?? null}</>;

  return (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      src={src}
      alt={alt}
      className={className}
      onError={(e) => {
        const target = e.currentTarget;
        target.style.display = 'none';
        // Show sibling fallback if exists
        const parent = target.parentElement;
        if (parent) {
          const fb = parent.querySelector('[data-fallback]') as HTMLElement | null;
          if (fb) fb.style.display = 'flex';
        }
      }}
    />
  );
}
