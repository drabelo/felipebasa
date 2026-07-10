(function(){
  "use strict";

  /* ---------- nav scroll state ---------- */
  var nav = document.getElementById('siteNav');
  var onScroll = function(){
    if (window.scrollY > 40) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  };
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- mobile nav toggle ---------- */
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  toggle.addEventListener('click', function(){
    toggle.classList.toggle('active');
    links.classList.toggle('open');
    nav.classList.toggle('menu-open');
  });
  links.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){
      toggle.classList.remove('active');
      links.classList.remove('open');
      nav.classList.remove('menu-open');
    });
  });

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting){
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: .12, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('is-visible'); });
  }

  /* ---------- skill bars ---------- */
  var bars = document.querySelectorAll('.bar-fill');
  if ('IntersectionObserver' in window){
    var barIo = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting){
          var w = entry.target.getAttribute('data-w') || 0;
          entry.target.style.width = w + '%';
          barIo.unobserve(entry.target);
        }
      });
    }, { threshold: .4 });
    bars.forEach(function(el){ barIo.observe(el); });
  } else {
    bars.forEach(function(el){ el.style.width = (el.getAttribute('data-w')||0) + '%'; });
  }

  /* ---------- lightbox with per-section groups, arrows, swipe, captions ---------- */
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxClose = document.getElementById('lightboxClose');
  var lightboxCaption = document.getElementById('lightboxCaption');
  var lightboxPrev = document.getElementById('lightboxPrev');
  var lightboxNext = document.getElementById('lightboxNext');
  var galleryImgs = document.querySelectorAll('.project-gallery img, .comp-card img, .art-images img, .project-hero img');

  var groups = [];
  galleryImgs.forEach(function(img){
    var section = img.closest('article, section') || document.body;
    var group = groups.find(function(g){ return g.section === section; });
    if (!group){ group = { section: section, imgs: [] }; groups.push(group); }
    img.dataset.group = groups.indexOf(group);
    img.dataset.index = group.imgs.length;
    group.imgs.push(img);
  });

  var current = { group: 0, index: 0 };

  function show(groupIdx, index){
    var imgs = groups[groupIdx].imgs;
    index = (index + imgs.length) % imgs.length;
    current = { group: groupIdx, index: index };
    var img = imgs[index];
    lightboxImg.src = img.currentSrc || img.src;
    lightboxImg.alt = img.alt || '';
    if (lightboxCaption){
      lightboxCaption.textContent = img.alt || '';
      lightboxCaption.style.display = img.alt ? '' : 'none';
    }
    var multiple = imgs.length > 1;
    if (lightboxPrev) lightboxPrev.style.display = multiple ? '' : 'none';
    if (lightboxNext) lightboxNext.style.display = multiple ? '' : 'none';
  }
  function openLightbox(groupIdx, index){
    show(groupIdx, index);
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox(){
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }
  function step(dir){ show(current.group, current.index + dir); }

  galleryImgs.forEach(function(img){
    img.addEventListener('click', function(){
      openLightbox(+img.dataset.group, +img.dataset.index);
    });
  });
  lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxPrev) lightboxPrev.addEventListener('click', function(e){ e.stopPropagation(); step(-1); });
  if (lightboxNext) lightboxNext.addEventListener('click', function(e){ e.stopPropagation(); step(1); });
  lightbox.addEventListener('click', function(e){
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', function(e){
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });

  var touchX = null;
  lightbox.addEventListener('touchstart', function(e){
    if (e.touches.length === 1) touchX = e.touches[0].clientX;
  }, { passive: true });
  lightbox.addEventListener('touchend', function(e){
    if (touchX === null) return;
    var dx = e.changedTouches[0].clientX - touchX;
    touchX = null;
    if (Math.abs(dx) > 48) step(dx > 0 ? -1 : 1);
  }, { passive: true });

  /* ---------- hero parallax + load moment ---------- */
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var heroBg = document.querySelector('.hero-bg');
  if (heroBg && !reduceMotion){
    document.body.classList.add('js-loaded');
    var ticking = false;
    var parallax = function(){
      var y = window.scrollY;
      if (y < window.innerHeight * 1.2){
        heroBg.style.transform = 'translateY(' + (y * 0.28).toFixed(1) + 'px) scale(1.08)';
      }
      ticking = false;
    };
    document.addEventListener('scroll', function(){
      if (!ticking){ requestAnimationFrame(parallax); ticking = true; }
    }, { passive: true });
    parallax();
  }

  /* ---------- smooth-scroll offset for fixed nav on anchor click ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = a.getAttribute('href').slice(1);
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      var y = target.getBoundingClientRect().top + window.pageYOffset - 76;
      window.scrollTo({ top: y, behavior: 'smooth' });
    });
  });
})();
