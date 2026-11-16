---
name: Clinical Precision
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#bacac5'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#85948f'
  outline-variant: '#3b4a46'
  surface-tint: '#38ddc4'
  primary: '#44e5cc'
  on-primary: '#003730'
  primary-container: '#00c9b1'
  on-primary-container: '#004f44'
  inverse-primary: '#006b5d'
  secondary: '#bac7dd'
  on-secondary: '#243142'
  secondary-container: '#3a485a'
  on-secondary-container: '#a8b6cb'
  tertiary: '#ffc474'
  on-tertiary: '#452b00'
  tertiary-container: '#f1a31f'
  on-tertiary-container: '#613e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#5ffae0'
  primary-fixed-dim: '#38ddc4'
  on-primary-fixed: '#00201b'
  on-primary-fixed-variant: '#005046'
  secondary-fixed: '#d6e3fa'
  secondary-fixed-dim: '#bac7dd'
  on-secondary-fixed: '#0f1c2c'
  on-secondary-fixed-variant: '#3a485a'
  tertiary-fixed: '#ffddb4'
  tertiary-fixed-dim: '#ffb955'
  on-tertiary-fixed: '#291800'
  on-tertiary-fixed-variant: '#633f00'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  title-lg:
    fontFamily: DM Sans
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
  body-lg:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: DM Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  caption:
    fontFamily: DM Sans
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 2rem
  gutter: 1.5rem
  sidebar-width: 280px
  stack-gap: 1rem
  section-gap: 2.5rem
---

## Brand & Style

This design system is engineered for high-stakes medical environments, balancing the rigorous demands of healthcare data with a sophisticated, modern aesthetic. The brand personality is clinical, authoritative, and technologically advanced. It moves away from the sterile, dated "hospital blue" in favor of a deep, high-contrast palette that reduces eye strain during long shifts.

The design style is **Modern Corporate with Glassmorphism**. It utilizes the structural stability of a dark-themed foundation (representing reliability and focus) layered with crisp, translucent white panels that evoke a sense of clarity and modern medical innovation. The emotional response is one of calm efficiency, precision, and trust. High-fidelity finishes like backdrop blurs and micro-interactions reinforce the product's position as a premium, next-generation medical tool.

## Colors

The palette is anchored by **Deep Navy (#0B1929)**, which serves as the primary canvas for the application, providing a solid, professional base that minimizes glare. **Electric Teal (#00C9B1)** is used exclusively for primary actions, success states, and progress indicators, creating a high-contrast focal point that guides the user's eye.

**Soft Amber (#F5A623)** is reserved for cautionary alerts and pending tasks, ensuring they are visible without causing unnecessary alarm. The neutral palette consists of high-clarity whites and cool grays used for typography and panel backgrounds. Semi-transparent white layers (80–90% opacity) are used over the navy background to create "Glass" surfaces that maintain a clinical, sterile feel while allowing the depth of the interface to show through.

## Typography

This design system employs a sophisticated typographic pairing to differentiate between "Editorial/Status" and "Operational/Data" content. 

**Playfair Display** is utilized for high-level dashboard headings and page titles. Its elegant, high-contrast serifs provide an authoritative, humanistic touch to the clinical interface, making the software feel premium and curated.

**DM Sans** is the workhorse font for all functional UI elements. Its low-contrast, geometric shapes ensure maximum legibility for patient records, dosages, and diagnostic data. Labels use a bold, slightly tracked-out treatment to ensure they are scannable at a glance.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid** model. The sidebar remains fixed at 280px, while the main content area utilizes a fluid 12-column grid. This allows the dense medical data to expand and utilize the full width of widescreen medical monitors while maintaining readable line lengths for patient notes.

A 4px baseline grid ensures rigorous vertical rhythm. Margins and gutters are generous (24px - 32px) to prevent the UI from feeling claustrophobic, which is critical in high-stress medical environments. 

**Breakpoints:**
- **Desktop (1200px+):** Full 12-column display with expanded sidebar.
- **Tablet (768px - 1199px):** 8-column grid, sidebar collapses to icons-only.
- **Mobile (<767px):** 4-column fluid layout, sidebar hidden behind a hamburger menu, headline-lg scales down to 24px.

## Elevation & Depth

Depth is established through **Glassmorphism and Tonal Layering** rather than traditional shadows. This maintains a clean, "sanitized" aesthetic.

1.  **Level 0 (Base):** Solid #0B1929.
2.  **Level 1 (Sidebars/Navigation):** #0B1929 with a subtle right-hand border (1px, 10% white).
3.  **Level 2 (Main Panels):** White (#FFFFFF) at 90% opacity with a `backdrop-filter: blur(12px)`. These panels feature a 1px solid white border at 20% opacity to define the edge against the dark background.
4.  **Level 3 (Modals/Popovers):** Pure white panels with a subtle Electric Teal outer glow (4px blur, 10% opacity) to indicate active focus.

Avoid heavy, dark shadows. Use light-based depth (inner glows and translucent borders) to create the "glass" effect.

## Shapes

The shape language is **Soft and Precise**. A 4px (0.25rem) base radius is applied to most UI components including buttons, inputs, and cards. This small radius provides a modern touch while maintaining the professional, "square" feel required for medical software. 

- **Buttons & Inputs:** 4px radius.
- **Data Tables:** 0px radius on internal cells, 4px on the container.
- **Avatars:** Circular (Pill-shaped) for medical staff; 4px rounded square for medical facilities.

## Components

- **Buttons:** Primary buttons use a solid Electric Teal background with white text. Secondary buttons use a transparent background with a teal border and teal text. 
- **Floating Label Inputs:** Use a 1px soft gray border. Upon focus, the border transitions to 2px Electric Teal, and the label floats to the top-left with a teal color.
- **Tables:** Data-dense tables feature "Zebra Striping." Use #F8FAFC for the base row and #F1F5F9 for the alternate. Hovering over a row highlights it with a 2px Electric Teal left-edge border and a subtle light-blue background tint.
- **Chips:** Used for patient status (e.g., "Stable," "Critical"). Status chips use a subtle background tint of the status color (e.g., Soft Amber at 10% opacity) with high-contrast bold text.
- **Sidebars:** Persistent Dark Navy (#0B1929) with Lucide icons in white (60% opacity). Active states use Electric Teal for the icon and a solid Teal 4px vertical bar on the left.
- **Medical Icons:** Use Lucide icons with a 1.5px stroke width for a clean, light appearance.
- **Cards:** White glassmorphic panels with `backdrop-blur`. Ensure text contrast meets WCAG AA standards against the blurred navy background.