<script setup>
import Button from './Button.vue'
</script>

<template>
    <section class="intro">
        <p class="greeting"><span class="arrow">></span> Hello, i'm</p>
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
    color: var(--text-tertiary);
    margin-bottom: 0.5rem;
    font-weight: 400;
    letter-spacing: 0.5px;
}

.greeting .arrow {
    color: var(--accent-green);
    font-size: 0.9rem;
    margin-right: 0.5rem;
}

.name {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.5rem 0;
    line-height: 1.2;
    letter-spacing: -1px;
    position: relative;
}

.cursor {
    color: var(--accent-green);
    -webkit-text-fill-color: var(--accent-green);
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
    font-size: 2rem;
    font-weight: 500;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 0.5rem;
    letter-spacing: 1px;
}

.info {
    font-size: 1.1rem;
    color: var(--text-tertiary);
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
        margin-top: 80px;
        min-height: calc(100vh - 80px);
    }

    .greeting {
        font-size: 1rem;
    }

    .name {
        font-size: 2.5rem;
        letter-spacing: -0.5px;
    }

    .title {
        font-size: 1.4rem;
    }

    .info {
        font-size: 1rem;
        max-width: 100%;
        line-height: 1.7;
    }

    .button-group {
        flex-direction: column;
        width: 100%;
        gap: 1rem;
    }
}

@media (max-width: 480px) {
    .intro {
        padding: 1.5rem 1rem;
        margin-top: 70px;
        min-height: calc(100vh - 70px);
    }

    .greeting {
        font-size: 0.95rem;
    }

    .name {
        font-size: 2rem;
        letter-spacing: -0.5px;
    }

    .cursor {
        font-size: 1.8rem;
    }

    .title {
        font-size: 1.2rem;
    }

    .info {
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .button-group {
        gap: 0.75rem;
    }
}
</style>