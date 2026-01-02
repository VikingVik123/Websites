<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
    mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
    mobileMenuOpen.value = false
}
</script>

<template>
    <nav class="navbar">
        <div class="name">
            <h1><span class="green">VO</span>_</h1>
        </div>
        
        <!-- Hamburger Button -->
        <button class="hamburger" :class="{ active: mobileMenuOpen }" @click="toggleMobileMenu" aria-label="Toggle menu">
            <span></span>
            <span></span>
            <span></span>
        </button>
        
        <!-- Navigation Menu -->
        <ul :class="{ 'mobile-open': mobileMenuOpen }">
            <li><span class="number">01.</span> <a href="#techstack" @click="closeMobileMenu">Skills</a></li>
            <li><span class="number">02.</span> <a href="#projects" @click="closeMobileMenu">Experience</a></li>
            <li><span class="number">03.</span> <a href="#contact" @click="closeMobileMenu">Contact</a></li>
        </ul>
    </nav>
</template>

<style scoped>
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 3rem;
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
    border-bottom: 2px solid transparent;
    border-image: linear-gradient(90deg, #4a5568, #2d3748, #4a5568) 1;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
    font-family: 'Courier New', Courier, Monaco, monospace;
}

.navbar:hover {
    box-shadow: 0 6px 30px rgba(0, 0, 0, 0.7);
}

.name h1 {
    font-size: 2rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 2px;
    transition: all 0.3s ease;
    cursor: pointer;
}

.name h1 .green {
    color: #00ff00;
}

.name h1:hover {
    transform: scale(1.05);
}

ul {
    display: flex;
    list-style: none;
    gap: 2.5rem;
    margin: 0;
    padding: 0;
}

ul li {
    position: relative;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

ul li .number {
    color: #00ff00;
    font-weight: 600;
    font-size: 0.9rem;
}

ul li a {
    color: #e2e8f0;
    text-decoration: none;
    font-size: 1rem;
    font-weight: 500;
    padding: 0.5rem 0;
    position: relative;
    transition: all 0.3s ease;
    letter-spacing: 0.5px;
}

ul li a .number {
    color: #00ff00;
    font-weight: 600;
}

ul li a:hover {
    color: #ffffff;
    transform: translateY(-2px);
}

/* Hamburger Menu */
.hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
    z-index: 1001;
    transition: all 0.3s ease;
}

.hamburger span {
    width: 25px;
    height: 2px;
    background: #00ff00;
    transition: all 0.3s ease;
    border-radius: 2px;
}

.hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(7px, 7px);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
}

/* Responsive Design */
@media (max-width: 768px) {
    .navbar {
        padding: 1rem 1.5rem;
    }

    .name h1 {
        font-size: 1.5rem;
    }

    .hamburger {
        display: flex;
    }

    ul {
        position: fixed;
        top: 0;
        right: -100%;
        height: 100vh;
        width: 70%;
        max-width: 300px;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 2.5rem;
        padding: 2rem;
        transition: right 0.3s ease;
        box-shadow: -5px 0 20px rgba(0, 0, 0, 0.5);
        z-index: 1000;
    }

    ul.mobile-open {
        right: 0;
    }

    ul li {
        width: 100%;
        text-align: center;
    }

    ul li a {
        font-size: 1.1rem;
        padding: 1rem;
        display: block;
        width: 100%;
    }

    ul li a:active {
        background: rgba(0, 255, 0, 0.1);
        border-radius: 4px;
    }
}

@media (max-width: 480px) {
    .navbar {
        padding: 1rem;
    }

    ul {
        width: 80%;
    }
}
</style>