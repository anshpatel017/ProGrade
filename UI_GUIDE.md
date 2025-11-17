# ProGrade - UI/UX Guide

## 🎨 Design System

### Color Palette

#### Primary Colors
- **Primary**: `#6366f1` (Indigo)
- **Primary Dark**: `#4f46e5` (Dark Indigo)
- **Secondary**: `#8b5cf6` (Purple)

#### Status Colors
- **Success**: `#10b981` (Green)
- **Error**: `#ef4444` (Red)
- **Warning**: `#f59e0b` (Amber)

#### Neutral Colors
- **Background**: `#f8fafc` (Light Gray)
- **Card Background**: `#ffffff` (White)
- **Text Primary**: `#1e293b` (Dark Gray)
- **Text Secondary**: `#64748b` (Medium Gray)
- **Border**: `#e2e8f0` (Light Border)

### Gradients
- **Primary Gradient**: `linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)`
- **Used for**: Navbar, buttons, chips, progress bars

---

## 📐 Typography

### Font Family
```css
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif
```

### Font Sizes
- **H1**: 2.5rem (40px) - Page titles
- **H2**: 2rem (32px) - Section titles
- **H3**: 1.5rem (24px) - Card titles
- **H4**: 1.25rem (20px) - Subsection titles
- **Body**: 1rem (16px) - Regular text
- **Small**: 0.875rem (14px) - Helper text

### Font Weights
- **Regular**: 400
- **Medium**: 500
- **Semibold**: 600
- **Bold**: 700

---

## 🎯 Layout Components

### Navigation Bar
```
┌─────────────────────────────────────────────────┐
│ 📊 ProGrade  │  Dashboard  │  Repo Analyzer  │  Image Rater  │
└─────────────────────────────────────────────────┘
```
- **Background**: Gradient (indigo to purple)
- **Height**: 60px
- **Sticky**: Yes (stays at top when scrolling)
- **Text Color**: White
- **Active Link**: Underline indicator

### Hero Section
```
╔═════════════════════════════════════════════════╗
║                                                 ║
║   ProGrade - Unified Analysis Platform         ║
║   Analyze repositories and rate images         ║
║                                                 ║
╚═════════════════════════════════════════════════╝
```
- **Background**: Gradient
- **Text Color**: White
- **Padding**: 4rem vertical
- **Text Alignment**: Center

### Feature Cards
```
┌─────────────────────┐
│ 📊 Icon             │
│                     │
│ Card Title          │
│ Description text    │
│ • Feature 1         │
│ • Feature 2         │
│ • Feature 3         │
│ [Button]            │
└─────────────────────┘
```
- **Background**: White
- **Border**: 1px light gray
- **Shadow**: Subtle
- **Hover**: Lift up 5px, enhanced shadow
- **Border Radius**: 12px
- **Padding**: 2rem

### Result Cards
```
┌─────────────────────────────────────────┐
│ 🔍 Card Title                           │
├─────────────────────────────────────────┤
│ Label:  Value                           │
│ Label:  Value                           │
│ Label:  Value                           │
└─────────────────────────────────────────┘
```
- **Background**: White
- **Border**: 1px light gray
- **Shadow**: Medium
- **Border Radius**: 12px
- **Padding**: 1.5rem

---

## 🎨 Component Styles

### Buttons

#### Primary Button
```
┌──────────────────┐
│  🔍 Analyze      │
└──────────────────┘
```
- **Background**: Gradient (indigo to purple)
- **Text Color**: White
- **Padding**: 0.75rem 1.5rem
- **Border Radius**: 8px
- **Hover**: Lift up 2px, enhanced shadow
- **Transition**: 0.3s ease

#### Secondary Button
```
┌──────────────────┐
│  🔄 Reset        │
└──────────────────┘
```
- **Background**: Light gray
- **Text Color**: Dark gray
- **Hover**: Darker gray

### Chips/Tags
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Python      │  │ React       │  │ PostgreSQL  │
└─────────────┘  └─────────────┘  └─────────────┘
```
- **Background**: Gradient
- **Text Color**: White
- **Padding**: 0.5rem 1rem
- **Border Radius**: 20px
- **Font Size**: 0.875rem

### Progress Bars
```
Confidence: 92%
┌────────────────────────────────────────┐
│████████████████████████░░░░░░░░░░░░░░░░│
└────────────────────────────────────────┘
```
- **Background**: Light gray
- **Fill**: Gradient
- **Height**: 8px
- **Border Radius**: 4px

### Loading Spinner
```
    ⟳
  Analyzing...
```
- **Animation**: Rotating 360° continuously
- **Duration**: 1s
- **Color**: Indigo
- **Size**: 50px

---

## 📱 Responsive Breakpoints

### Desktop (1200px+)
- Full width layouts
- 3-column grids
- Large typography
- Sidebar navigation

### Tablet (768px - 1199px)
- 2-column grids
- Adjusted padding
- Medium typography
- Hamburger menu ready

### Mobile (< 768px)
- 1-column layouts
- Reduced padding
- Smaller typography
- Touch-friendly buttons
- Full-width inputs

---

## 🎬 Animations

### Transitions
```css
transition: all 0.3s ease;
```
- Applied to: Buttons, cards, links
- Duration: 300ms
- Timing: Ease (smooth)

### Hover Effects
- **Cards**: `transform: translateY(-5px)`
- **Buttons**: `transform: translateY(-2px)`
- **Links**: `opacity: 0.8`

### Loading Animation
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}
animation: spin 1s linear infinite;
```

### Fade In
- Used for: Results section
- Duration: 0.3s

---

## 📋 Page Layouts

### Dashboard (index.html)
```
┌─────────────────────────────────────┐
│         Navigation Bar              │
├─────────────────────────────────────┤
│                                     │
│         Hero Section                │
│                                     │
├─────────────────────────────────────┤
│  Feature Card 1  │  Feature Card 2  │
├─────────────────────────────────────┤
│         How It Works                │
│  Step 1  │  Step 2  │  Step 3  │   │
├─────────────────────────────────────┤
│         Footer                      │
└─────────────────────────────────────┘
```

### Repository Analyzer (repo_analyzer.html)
```
┌─────────────────────────────────────┐
│         Navigation Bar              │
├─────────────────────────────────────┤
│  Repository Analyzer                │
│  [Input Form]                       │
├─────────────────────────────────────┤
│  [Loading Spinner] OR [Results]     │
│  ┌─────────────┐  ┌─────────────┐  │
│  │ Summary     │  │ Scores      │  │
│  └─────────────┘  └─────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ Tech Stack                   │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ Contributors                 │  │
│  └──────────────────────────────┘  │
├─────────────────────────────────────┤
│         Footer                      │
└─────────────────────────────────────┘
```

### Image Rater (image_rater.html)
```
┌─────────────────────────────────────┐
│         Navigation Bar              │
├─────────────────────────────────────┤
│  Image Quality Rater                │
│  [File Upload Area]                 │
├─────────────────────────────────────┤
│  [Loading Spinner] OR [Results]     │
│  ┌──────────────────────────────┐  │
│  │ Image Preview                │  │
│  └──────────────────────────────┘  │
│  ┌─────────────┐  ┌─────────────┐  │
│  │ Rating      │  │ Confidence  │  │
│  │ ★★★★☆      │  │ 92%         │  │
│  └─────────────┘  └─────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ Details                      │  │
│  └──────────────────────────────┘  │
├─────────────────────────────────────┤
│         Footer                      │
└─────────────────────────────────────┘
```

---

## 🎯 Form Elements

### Text Input
```
Label
┌──────────────────────────────────────┐
│ Placeholder text...                  │
└──────────────────────────────────────┘
Helper text
```
- **Border**: 1px light gray
- **Focus**: Blue border + shadow
- **Padding**: 0.75rem
- **Border Radius**: 8px

### File Upload
```
┌──────────────────────────────────────┐
│  ☁️ Click to upload or drag & drop   │
│  PNG, JPG, JPEG, GIF (Max 50MB)     │
└──────────────────────────────────────┘
```
- **Border**: 2px dashed
- **Hover**: Indigo border + light background
- **Padding**: 2rem
- **Border Radius**: 8px

### Select/Dropdown
- **Style**: Native browser
- **Padding**: 0.75rem
- **Border**: 1px light gray

---

## 🌙 Dark Mode Ready

The CSS uses CSS variables, making dark mode easy to implement:

```css
:root {
  --primary-color: #6366f1;
  --bg-color: #f8fafc;
  --text-primary: #1e293b;
}

@media (prefers-color-scheme: dark) {
  :root {
    --primary-color: #818cf8;
    --bg-color: #1e293b;
    --text-primary: #f1f5f9;
  }
}
```

---

## ♿ Accessibility Features

### Semantic HTML
- `<nav>` for navigation
- `<main>` for main content
- `<section>` for sections
- `<footer>` for footer

### ARIA Labels
- Form labels linked to inputs
- Buttons have clear text
- Icons have title attributes

### Keyboard Navigation
- Tab through all interactive elements
- Enter to submit forms
- Escape to close modals

### Color Contrast
- Text: 4.5:1 ratio (WCAG AA)
- Links: Underlined for clarity
- Icons: Accompanied by text

---

## 📊 Data Visualization

### Tech Stack Chips
```
Languages:  [Python]  [JavaScript]  [Java]
Frameworks: [React]   [Django]      [Spring]
Databases:  [PostgreSQL] [MongoDB]
```

### Ratings
```
⭐⭐⭐⭐☆  4.0 / 5.0
```

### Progress
```
Confidence: 92%
████████████████████░░░░░░░░░░░░░░░░░░
```

### Lists
```
1. First contributor — 150 commits
2. Second contributor — 120 commits
3. Third contributor — 95 commits
```

---

## 🎨 CSS Classes Reference

### Layout
- `.container` - Max-width container
- `.navbar` - Navigation bar
- `.hero` - Hero section
- `.footer` - Footer

### Components
- `.btn` - Button base
- `.btn-primary` - Primary button
- `.btn-secondary` - Secondary button
- `.card` - Card component
- `.chip` - Tag/chip component

### Utilities
- `.loading-spinner` - Loading indicator
- `.alert` - Alert message
- `.alert-error` - Error alert
- `.progress-bar` - Progress indicator
- `.muted` - Muted text

### Grids
- `.features-grid` - Feature cards grid
- `.results-grid` - Results cards grid
- `.steps` - Steps grid
- `.chips` - Chips container

---

## 🔧 Customization Tips

### Change Primary Color
Edit `style.css`:
```css
:root {
  --primary-color: #your-color;
  --primary-dark: #your-dark-color;
  --secondary-color: #your-secondary;
}
```

### Change Font
Edit `body` in `style.css`:
```css
body {
  font-family: 'Your Font', sans-serif;
}
```

### Change Spacing
Edit CSS variables:
```css
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
```

### Add Dark Mode
Add media query:
```css
@media (prefers-color-scheme: dark) {
  :root {
    /* dark mode colors */
  }
}
```

---

## 📱 Mobile Optimization

### Touch Targets
- Minimum 44x44px for buttons
- Adequate spacing between clickables
- Large text for readability

### Performance
- Minimal animations on mobile
- Optimized images
- Lazy loading ready

### Viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## ✨ Summary

The ProGrade UI features:
- ✅ Modern gradient design
- ✅ Responsive layout
- ✅ Smooth animations
- ✅ Accessible components
- ✅ Professional appearance
- ✅ Mobile-friendly
- ✅ Dark mode ready
- ✅ Easy to customize

**Result**: A professional, modern web application that looks great on all devices!
