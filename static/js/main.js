// main.js - Main JavaScript functionality

document.addEventListener("DOMContentLoaded", () => {
  // Initialize all components
  initNavbar()
  initDarkMode()
  initAnimations()
  initSkillBars()
  initContactForm()
  initProjectFilters()
})

// Navbar functionality
function initNavbar() {
  const header = document.querySelector(".header")
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn")
  const mobileMenu = document.querySelector(".mobile-menu")

  // Handle scroll
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("scrolled")
    } else {
      header.classList.remove("scrolled")
    }
  })

  // Mobile menu toggle
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("active")

      // Toggle aria-expanded
      const expanded = mobileMenuBtn.getAttribute("aria-expanded") === "true" || false
      mobileMenuBtn.setAttribute("aria-expanded", !expanded)

      // Toggle menu icon
      const menuIcon = mobileMenuBtn.querySelector(".menu-icon")
      const closeIcon = mobileMenuBtn.querySelector(".close-icon")

      if (menuIcon && closeIcon) {
        menuIcon.classList.toggle("hidden")
        closeIcon.classList.toggle("hidden")
      }
    })
  }
}

// Dark mode toggle
function initDarkMode() {
  const darkModeToggle = document.querySelector(".dark-mode-toggle")
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)")

  // Check for saved theme preference or use OS preference
  const savedTheme = localStorage.getItem("theme")

  if (savedTheme === "dark" || (!savedTheme && prefersDarkScheme.matches)) {
    document.body.classList.add("dark-mode")
    updateDarkModeIcon(true)
  }

  // Toggle dark mode on button click
  if (darkModeToggle) {
    darkModeToggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode")

      const isDarkMode = document.body.classList.contains("dark-mode")
      localStorage.setItem("theme", isDarkMode ? "dark" : "light")

      updateDarkModeIcon(isDarkMode)
    })
  }

  // Update icon based on current mode
  function updateDarkModeIcon(isDarkMode) {
    if (!darkModeToggle) return

    const sunIcon = darkModeToggle.querySelector(".sun-icon")
    const moonIcon = darkModeToggle.querySelector(".moon-icon")

    if (sunIcon && moonIcon) {
      if (isDarkMode) {
        sunIcon.classList.remove("hidden")
        moonIcon.classList.add("hidden")
      } else {
        sunIcon.classList.add("hidden")
        moonIcon.classList.remove("hidden")
      }
    }
  }
}

// Animations on scroll
function initAnimations() {
  const animatedElements = document.querySelectorAll(".animate-on-scroll")

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animated")
          observer.unobserve(entry.target)
        }
      })
    },
    {
      threshold: 0.1,
    },
  )

  animatedElements.forEach((element) => {
    observer.observe(element)
  })
}

// Skill bars animation
function initSkillBars() {
  const skillBars = document.querySelectorAll(".skill-progress")

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const progressBar = entry.target
          const percentage = progressBar.getAttribute("data-percentage")
          progressBar.style.width = percentage + "%"
          observer.unobserve(progressBar)
        }
      })
    },
    {
      threshold: 0.1,
    },
  )

  skillBars.forEach((bar) => {
    observer.observe(bar)
  })
}

// Contact form validation and submission
function initContactForm() {
  const contactForm = document.querySelector(".contact-form")

  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      const nameInput = contactForm.querySelector("#name")
      const emailInput = contactForm.querySelector("#email")
      const messageInput = contactForm.querySelector("#message")

      let isValid = true

      // Simple validation
      if (!nameInput.value.trim()) {
        showInputError(nameInput, "Name is required")
        isValid = false
      } else {
        clearInputError(nameInput)
      }

      if (!emailInput.value.trim()) {
        showInputError(emailInput, "Email is required")
        isValid = false
      } else if (!isValidEmail(emailInput.value.trim())) {
        showInputError(emailInput, "Please enter a valid email")
        isValid = false
      } else {
        clearInputError(emailInput)
      }

      if (!messageInput.value.trim()) {
        showInputError(messageInput, "Message is required")
        isValid = false
      } else {
        clearInputError(messageInput)
      }

      // If using AJAX submission, prevent default and handle manually
      if (!isValid) {
        e.preventDefault()
      }
    })

    // Helper functions for form validation
    function showInputError(input, message) {
      const formGroup = input.closest(".form-group")
      const errorElement = formGroup.querySelector(".error-message") || document.createElement("div")

      errorElement.className = "error-message text-red-500 text-sm mt-1"
      errorElement.textContent = message

      if (!formGroup.querySelector(".error-message")) {
        formGroup.appendChild(errorElement)
      }

      input.classList.add("border-red-500")
    }

    function clearInputError(input) {
      const formGroup = input.closest(".form-group")
      const errorElement = formGroup.querySelector(".error-message")

      if (errorElement) {
        formGroup.removeChild(errorElement)
      }

      input.classList.remove("border-red-500")
    }

    function isValidEmail(email) {
      const re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    }
  }
}

// Project filtering
function initProjectFilters() {
  const filterButtons = document.querySelectorAll(".project-filter-btn")
  const projectItems = document.querySelectorAll(".project-item")

  if (filterButtons.length && projectItems.length) {
    filterButtons.forEach((button) => {
      button.addEventListener("click", function () {
        // Remove active class from all buttons
        filterButtons.forEach((btn) => btn.classList.remove("active"))

        // Add active class to clicked button
        this.classList.add("active")

        const filter = this.getAttribute("data-filter")

        // Filter projects
        projectItems.forEach((item) => {
          if (filter === "all") {
            item.style.display = "block"
          } else {
            const categories = item.getAttribute("data-categories").split(",")
            if (categories.includes(filter)) {
              item.style.display = "block"
            } else {
              item.style.display = "none"
            }
          }
        })
      })
    })
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const filterButtons = document.querySelectorAll(".project-filter-btn")
  const projectItems = document.querySelectorAll(".project-item")

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Remove active class from all buttons
      filterButtons.forEach((btn) => btn.classList.remove("active"))

      // Add active class to clicked button
      this.classList.add("active")

      const filter = this.getAttribute("data-filter")

      // Filter projects
      projectItems.forEach((item) => {
        if (filter === "all") {
          item.style.display = "block"
        } else {
          const categories = item.getAttribute("data-categories").split(",")
          if (categories.includes(filter)) {
            item.style.display = "block"
          } else {
            item.style.display = "none"
          }
        }
      })
    })
  })

  // Animation on scroll
  const animateElements = document.querySelectorAll(".animate-on-scroll")

  function checkIfInView() {
    animateElements.forEach((element) => {
      const elementTop = element.getBoundingClientRect().top
      const elementVisible = 150

      if (elementTop < window.innerHeight - elementVisible) {
        element.classList.add("active")
      }
    })
  }

  window.addEventListener("scroll", checkIfInView)
  checkIfInView() // Check on page load
})

