<div align="center">

# Golden Hour Coffee Co.

**A cozy, sunlit neighborhood café website built with React, TypeScript, and Tailwind CSS.**

[![Deployed on Vercel](https://img.shields.io/badge/Deployed-Vercel-black?logo=vercel)](#)
[![React 19](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?logo=typescript)](https://www.typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.1-06B6D4?logo=tailwindcss)](https://tailwindcss.com)

</div>

---

A responsive single-page website for **Golden Hour Coffee Co.** — a neighborhood brunch café in East Austin, Texas. Features a warm terracotta color palette, smooth page transitions, a full menu with categories, photo gallery, reservation system, and an AI-powered chat assistant powered by Google Gemini.

## Features

- **6 pages** — Home, Menu, Reservations, Gallery, About, Contact
- **Animated transitions** — Framer Motion page transitions and scroll-triggered animations
- **Responsive design** — Mobile-first layout with Tailwind CSS
- **Menu system** — Coffee, brunch, and lunch items with filtering and images
- **Reservation form** — Date, time, guest count with confirmation feedback
- **Photo gallery** — Masonry grid with lightbox and Instagram embeds
- **Back-to-top** — Floating button appears on scroll
- **Accessibility** — Skip-to-content link, semantic HTML, keyboard navigation
- **SEO-ready** — Open Graph tags, meta descriptions, theme color

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 19 |
| Language | TypeScript 5.8 |
| Styling | Tailwind CSS 4.1 |
| Animations | Framer Motion (`motion`) |
| Icons | Lucide React |
| Build | Vite 6 |
| AI | Google Gemini API (`@google/genai`) |
| Server | Express (API routes) |

## Project Structure

```
goldenhour/
├── public/
│   └── favicon.svg          # Terracotta "G" favicon
├── src/
│   ├── components/
│   │   ├── Header.tsx        # Sticky nav with page links
│   │   ├── Home.tsx           # Hero, featured items, testimonials
│   │   ├── Menu.tsx           # Filterable menu with categories
│   │   ├── Reservations.tsx   # Booking form with validation
│   │   ├── Gallery.tsx        # Masonry photo grid
│   │   ├── About.tsx          # Café story and values
│   │   ├── Contact.tsx        # Contact info and form
│   │   ├── Footer.tsx         # Site footer with links
│   │   └── ErrorBoundary.tsx  # Error fallback UI
│   ├── App.tsx                # Root component, routing, transitions
│   ├── main.tsx               # Entry point
│   ├── data.ts                # Menu items, gallery, testimonials
│   └── types.ts               # TypeScript interfaces
├── index.html                 # HTML shell with meta tags
├── metadata.json              # App metadata
├── package.json               # Dependencies and scripts
├── tsconfig.json              # TypeScript config
└── vite.config.ts             # Vite build config
```

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) 18+
- A [Google AI Studio](https://ai.google.dev/) API key (optional, for AI features)

### Installation

```bash
git clone https://github.com/Ibra106i/goldenhour.git
cd goldenhour
npm install
```

### Environment Variables

Copy the example env file and fill in your keys:

```bash
cp .env.example .env.local
```

```env
GEMINI_API_KEY=your_gemini_api_key_here
APP_URL=http://localhost:3000
```

### Development

```bash
npm run dev
```

Opens at [http://localhost:3000](http://localhost:3000).

### Production

```bash
npm run build       # Build to dist/
npm run preview     # Preview the production build
npm run lint        # Type-check with tsc --noEmit
npm run clean       # Remove dist/ and server.js
```

## Brand Identity

| Element | Value |
|---------|-------|
| Primary color | Terracotta `#C1633D` |
| Background | Warm cream |
| Typography | System font stack |
| Tagline | "Slow mornings, strong coffee" |
| Hook word | "Linger" |
| Aesthetic | Quiet premium, confidence through restraint |

## Deployment

The site is configured for [Vercel](https://vercel.com) deployment. Push to `main` to trigger a deploy.

## License

Built with [Google AI Studio](https://ai.google.dev/) and Vercel.
