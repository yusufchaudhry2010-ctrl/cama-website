/* ===================================================
   CHILTERN ACADEMY OF MARTIAL ARTS — MAIN JS
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ── NAVBAR SCROLL ─────────────────────────────── */
  const navbar = document.getElementById('navbar');
  const handleScroll = () => {
    if (navbar) {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* ── HAMBURGER ──────────────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const navLinks  = document.getElementById('nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);
    });
    // Close on link click
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => navLinks.classList.remove('open'));
    });
  }

  /* ── PARTICLE SYSTEM ────────────────────────────── */
  const canvas = document.getElementById('particleCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let W, H, particles = [];

    const resize = () => {
      W = canvas.width  = window.innerWidth;
      H = canvas.height = window.innerHeight;
    };
    window.addEventListener('resize', resize);
    resize();

    class Particle {
      constructor() { this.reset(); }
      reset() {
        this.x  = Math.random() * W;
        this.y  = Math.random() * H;
        this.vx = (Math.random() - 0.5) * 0.4;
        this.vy = (Math.random() - 0.5) * 0.4;
        this.r  = Math.random() * 1.5 + 0.5;
        this.life = 1;
        this.decay = Math.random() * 0.003 + 0.001;
        this.color = Math.random() > 0.7 ? '#c8102e' : '#d4a017';
      }
      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life -= this.decay;
        if (this.life <= 0 || this.x < 0 || this.x > W || this.y < 0 || this.y > H) this.reset();
      }
      draw() {
        ctx.save();
        ctx.globalAlpha = this.life * 0.6;
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }
    }

    for (let i = 0; i < 80; i++) particles.push(new Particle());

    const animate = () => {
      ctx.clearRect(0, 0, W, H);
      // Draw subtle connection lines
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 100) {
            ctx.save();
            ctx.globalAlpha = (1 - dist / 100) * 0.08;
            ctx.strokeStyle = '#c8102e';
            ctx.lineWidth = 0.5;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
            ctx.restore();
          }
        }
        particles[i].update();
        particles[i].draw();
      }
      requestAnimationFrame(animate);
    };
    animate();
  }

  /* ── COUNTER ANIMATION ──────────────────────────── */
  const counters = document.querySelectorAll('.stat-number[data-target]');
  let countersStarted = false;

  const startCounters = () => {
    if (countersStarted) return;
    const statsEl = document.getElementById('stats');
    if (!statsEl) return;
    const rect = statsEl.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      countersStarted = true;
      counters.forEach(counter => {
        const target = parseInt(counter.dataset.target);
        const duration = 2000;
        const start = performance.now();
        const tick = (now) => {
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          counter.textContent = Math.floor(eased * target);
          if (progress < 1) requestAnimationFrame(tick);
          else counter.textContent = target;
        };
        requestAnimationFrame(tick);
      });
    }
  };
  window.addEventListener('scroll', startCounters, { passive: true });
  startCounters();

  /* ── SCROLL REVEAL ──────────────────────────────── */
  const revealEls = document.querySelectorAll(
    '.class-card, .instructor-card, .testimonial-card, ' +
    '.about-image-col, .about-content-col, ' +
    '.instructor-full-card, .stat-item, .section-header, ' +
    '.discipline-info-text, .schedule-card, .discipline-pill'
  );

  revealEls.forEach((el, i) => {
    el.classList.add('reveal');
    el.style.transitionDelay = `${(i % 4) * 0.08}s`;
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  /* ── CURSOR GLOW ────────────────────────────────── */
  const cursorGlow = document.createElement('div');
  cursorGlow.style.cssText = `
    position: fixed;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(200,16,46,0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    transform: translate(-50%, -50%);
    transition: opacity 0.3s;
    will-change: transform;
  `;
  document.body.appendChild(cursorGlow);

  let mx = 0, my = 0, cx = 0, cy = 0;
  document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
  const moveCursor = () => {
    cx += (mx - cx) * 0.08;
    cy += (my - cy) * 0.08;
    cursorGlow.style.left = cx + 'px';
    cursorGlow.style.top  = cy + 'px';
    requestAnimationFrame(moveCursor);
  };
  moveCursor();

  /* ── ACTIVE NAV LINK ────────────────────────────── */
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (href === path || (path === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  /* ── BOOKING FORM ───────────────────────────────── */
  // Form submission is now handled via standard HTML POST to ensure FormSubmit.co activates properly

  /* ── PUNCH EFFECT ON HERO ───────────────────────── */
  const heroBtns = document.querySelectorAll('.hero-buttons .btn');
  heroBtns.forEach(btn => {
    btn.addEventListener('mouseenter', () => {
      btn.style.transform = 'translateY(-4px) scale(1.04)';
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = '';
    });
  });

  // Hero Slideshow
  const slides = document.querySelectorAll('.hero-bg.slideshow .slide');
  if (slides.length > 1) {
    let currentSlide = window.camaStartSlide !== undefined ? window.camaStartSlide : 0;

    setInterval(() => {
      slides[currentSlide].classList.remove('show');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('show');
    }, 5000); // Change image every 5 seconds
  }

});
