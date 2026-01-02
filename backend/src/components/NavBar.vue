<script setup>

</script>

<template>
    <nav class="navbar">
        <div class="name">
            <h1><span class="green">VO</span>_</h1>
        </div>
        <ul>
            <li><span class="number">01.</span> <a href="#skills">Skills</a></li>
            <li><span class="number">02.</span> <a href="#projects">Projects</a></li>
            <li><span class="number">03.</span> <a href="#contact">Contact</a></li>
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

ul li a::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 2px;
    background: #00ff00;
    transition: width 0.3s ease;
}

ul li a:hover {
    color: #ffffff;
    transform: translateY(-2px);
}

ul li a:hover::after {
    width: 100%;
}

/* Responsive Design */
@media (max-width: 768px) {
    .navbar {
        padding: 1rem 1.5rem;
    }

    .name h1 {
        font-size: 1.5rem;
    }

    ul {
        gap: 1.5rem;
    }

    ul li a {
        font-size: 0.9rem;
    }
}

@media (max-width: 480px) {
    .navbar {
        padding: 1rem;
    }

    ul {
        gap: 1rem;
    }

    ul li a {
        font-size: 0.85rem;
        gap: 0.3rem;
    }
}
</style>