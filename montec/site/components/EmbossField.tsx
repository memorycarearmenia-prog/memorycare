'use client'

import { useEffect, useRef } from 'react'

/**
 * The signature element.
 *
 * The brand's own law for its mark is that it is applied as a blind emboss —
 * "visible only through light and shadow, never through colour contrast".
 * This renders that law rather than describing it: the real emboss photograph
 * sits in near-darkness, and a soft light follows the pointer, revealing the
 * grain and the mark only where it falls.
 *
 * Degradation is deliberate: with no pointer (touch) or with reduced motion
 * requested, the light rests slightly off-centre and stays there — the mark is
 * still readable, it simply stops following.
 */
export function EmbossField({
  src,
  className = '',
  intensity = 1,
}: {
  src: string
  className?: string
  /** 0–1 multiplier on how far the reveal reaches. */
  intensity?: number
}) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return

    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const fine = window.matchMedia('(pointer: fine)').matches
    if (reduced || !fine) return

    let raf = 0
    const onMove = (e: PointerEvent) => {
      const rect = el.getBoundingClientRect()
      const x = ((e.clientX - rect.left) / rect.width) * 100
      const y = ((e.clientY - rect.top) / rect.height) * 100
      cancelAnimationFrame(raf)
      raf = requestAnimationFrame(() => {
        el.style.setProperty('--mx', `${x}%`)
        el.style.setProperty('--my', `${y}%`)
      })
    }

    el.addEventListener('pointermove', onMove)
    return () => {
      el.removeEventListener('pointermove', onMove)
      cancelAnimationFrame(raf)
    }
  }, [])

  const reach = `${26 * intensity}%`

  return (
    <div
      ref={ref}
      aria-hidden="true"
      className={`pointer-events-auto absolute inset-0 overflow-hidden ${className}`}
      style={{ ['--mx' as string]: '62%', ['--my' as string]: '46%' }}
    >
      {/* The material, all but unlit. */}
      <div
        className="absolute inset-0 bg-cover bg-center"
        style={{ backgroundImage: `url(${src})`, filter: 'brightness(0.16) saturate(0.4) contrast(1.1)' }}
      />
      {/* The same material under the light — revealed only where the light falls. */}
      <div
        className="absolute inset-0 bg-cover bg-center transition-[opacity] duration-700 ease-quiet"
        style={{
          backgroundImage: `url(${src})`,
          filter: 'brightness(0.72) saturate(0.75) contrast(1.05)',
          maskImage: `radial-gradient(circle ${reach} at var(--mx) var(--my), #000 0%, transparent 72%)`,
          WebkitMaskImage: `radial-gradient(circle ${reach} at var(--mx) var(--my), #000 0%, transparent 72%)`,
        }}
      />
      {/* Ground the type: the field darkens toward the left and the bottom. */}
      <div className="absolute inset-0 bg-gradient-to-r from-obsidian via-obsidian/85 to-obsidian/35" />
      <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-obsidian to-transparent" />
    </div>
  )
}
