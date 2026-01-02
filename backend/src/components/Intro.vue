<script setup>
import Button from './Button.vue'
</script>

<template>
    <section class="intro">
        <p class="greeting">Hello, i'm</p>
        <h1 class="name">Victor Odimmegwa<span class="cursor">|</span></h1>
        <p class="title">Backend Engineer</p>
        <p class="info">
            I build robust, scalable systems and APIs. 
            Passionate about distributed systems, database optimization, and clean architecture.
        </p>
        <div class="button-group">
            <Button href="#projects">View Projects</Button>
            <Button variant="outline" href="#contact">Contact</Button>
        </div>
    </section>
</template>

<style scoped>
.intro {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    min-height: 100vh;
    padding: 2rem 3rem;
    margin-top: 2rem; /* Account for fixed navbar */
}

.greeting {
    font-size: 1.2rem;
    color: #9ca3af;
    margin-bottom: 0.5rem;
    font-weight: 400;
    letter-spacing: 0.5px;
}

.name {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.5rem 0;
    line-height: 1.2;
    letter-spacing: -1px;
    position: relative;
}

.cursor {
    color: #00ff00;
    -webkit-text-fill-color: #00ff00;
    background: none;
    animation: blink 1s step-end infinite;
    margin-left: 0.1rem;
}

@keyframes blink {
    0%, 50% {
        opacity: 1;
    }
    51%, 100% {
        opacity: 0;
    }
}

.title {
    font-size: 1.5rem;
    color: #6b7280;
    font-weight: 500;
    margin-top: 0.5rem;
    letter-spacing: 1px;
}

.info {
    font-size: 1.1rem;
    color: #9ca3af;
    font-weight: 400;
    line-height: 1.8;
    max-width: 600px;
    margin-top: 1.5rem;
    letter-spacing: 0.3px;
}

.button-group {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .intro {
        padding: 2rem 1.5rem;
        margin-top: 70px;
    }

    .greeting {
        font-size: 1rem;
    }

    .name {
        font-size: 3rem;
    }

    .title {
        font-size: 1.2rem;
    }

    .info {
        font-size: 1rem;
        max-width: 100%;
    }

    .button-group {
        flex-direction: column;
        width: 100%;
    }
}

@media (max-width: 480px) {
    .intro {
        padding: 1.5rem 1rem;
    }

    .name {
        font-size: 2.5rem;
    }

    .title {
        font-size: 1rem;
    }

    .info {
        font-size: 0.95rem;
    }
}
</style>