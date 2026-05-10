'use client';

interface ClientImageProps {
  src: string;
  alt: string;
  className?: string;
  fallback?: string;
}

export default function ClientImage({ src, alt, className, fallback }: ClientImageProps) {
  return (
    <img
      src={src}
      alt={alt}
      className={className}
      onError={(e) => {
        const target = e.target as HTMLImageElement;
        if (fallback) {
          target.src = fallback;
        } else {
          target.style.display = 'none';
        }
      }}
    />
  );
}
