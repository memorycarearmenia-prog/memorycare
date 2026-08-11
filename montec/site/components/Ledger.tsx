"use client";

import Link from "next/link";
import { useState } from "react";
import { Price } from "./Bits";
import {
  products,
  indexOf,
  total,
  type Group,
} from "@/lib/products";

const order: Group[] = [
  "Carry",
  "Command center",
  "Financial",
  "Lifestyle",
  "Foundation",
];

const groupNote: Record<Group, string> = {
  Carry: "The pieces that travel with the decision",
  "Command center": "The desk, and what leaves it",
  Financial: "What money is kept in",
  Lifestyle: "The routine, kept intact",
  Foundation: "Worn, not carried",
};

/**
 * The batch reads as a manifest, not a shop grid: number, name, object, price.
 * Most luxury sites open with a wall of photographs; an inventory is truer to a
 * brand whose product page is literally called THE AUDIT — and it lets all
 * thirteen pieces be seen at once instead of four at a time.
 */
export function Ledger() {
  const [active, setActive] = useState<string | null>(null);

  return (
    <div className="lg:grid lg:grid-cols-[minmax(0,1fr)_340px] lg:gap-12">
      {/* The reveal: pinned beside the list on wide screens, in its own column —
          a float would let the first rows wrap around it and end up narrower
          than the rest of the manifest. */}
      <div className="hidden lg:block">
        <div className="pointer-events-none sticky top-24 h-[340px] w-[340px]">
          {products.map((p) => (
            <div
              key={p.slug}
              className={`absolute inset-0 bg-paper transition-opacity duration-500 ease-quiet ${
                active === p.slug ? "opacity-100" : "opacity-0"
              }`}
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={`/products/${p.slug}/three-quarter.webp`}
                alt=""
                className="h-full w-full object-cover"
                loading="lazy"
              />
            </div>
          ))}
          <div
            className={`absolute inset-0 flex items-center justify-center border border-brass/20 transition-opacity duration-500 ${
              active ? "opacity-0" : "opacity-100"
            }`}
          >
            <span className="text-[11px] uppercase tracking-wide2 text-paper/30">
              Thirteen pieces
            </span>
          </div>
        </div>
      </div>

      <div className="min-w-0 lg:order-first">
        {order.map((g) => {
          const rows = products.filter((p) => p.group === g);
          if (!rows.length) return null;
          return (
            <section key={g} className="mb-16">
              <div className="flex items-baseline gap-5 border-b border-brass/25 pb-3">
                <h2 className="font-serif text-[20px] text-brass">{g}</h2>
                <span className="text-[12px] text-paper/40">
                  {groupNote[g]}
                </span>
              </div>

              <ul>
                {rows.map((p) => (
                  <li key={p.slug}>
                    <Link
                      href={`/collection/${p.slug}/`}
                      onMouseEnter={() => setActive(p.slug)}
                      onMouseLeave={() => setActive(null)}
                      onFocus={() => setActive(p.slug)}
                      onBlur={() => setActive(null)}
                      className="group grid grid-cols-[3rem_1fr] items-baseline gap-x-5 gap-y-1 border-b border-paper/[0.07] py-6 transition-colors duration-300 hover:border-brass/40 md:grid-cols-[3.5rem_minmax(0,1fr)_9rem_10rem]"
                    >
                      <span className="text-[12px] tabular-nums text-paper/30 transition-colors group-hover:text-brass">
                        {indexOf(p.slug)}
                      </span>

                      <span className="min-w-0">
                        <span className="block font-serif text-[24px] leading-tight transition-colors duration-300 group-hover:text-brass md:text-[27px]">
                          {p.name}
                        </span>
                        <span className="mt-1 block font-serif text-[14px] italic text-paper/45">
                          {p.line}
                        </span>
                      </span>

                      <span className="col-start-2 text-[13px] text-paper/50 md:col-start-3">
                        {p.object}
                      </span>

                      <span className="col-start-2 text-[13px] text-paper/70 md:col-start-4 md:text-right">
                        <Price price={p.price} />
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </section>
          );
        })}

        <p className="text-[12px] uppercase tracking-wide2 text-paper/30">
          {total} pieces · Batch 001 · Prices in Armenian dram
        </p>
      </div>
    </div>
  );
}
