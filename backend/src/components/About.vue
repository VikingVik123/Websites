<script setup>

</script>

<template>
    <section class="about">
        <h2><span class="number">01.</span> About Me</h2>
        <p>
            I'm a backend-focused software engineer with hands-on experience designing and building scalable, production-grade systems across media streaming, and SaaS platforms.
            My work centers on translating real-world problems into reliable backend architectures using Python, modern frameworks, and cloud-native patterns.
        </p>
        <p>
            I value clean architecture, clear APIs, and solutions that scale predictably under load. Whether working on greenfield projects or improving existing systems, my focus is always on correctness, performance, and long-term maintainability. 
            I am actively seeking opportunities where I can contribute to impactful backend systems while continuing to grow as a software engineer.
        </p>
    </section>
</template>

<style scoped>
.about {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 3rem;
    max-width: 900px;
}

.about h2 {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: 0.5px;
}

.about h2 .number {
    color: var(--accent-green);
    font-size: 1.5rem;
    font-weight: 600;
}

.about p {
    font-size: 1.1rem;
    color: var(--text-tertiary);
    line-height: 1.8;
    margin-bottom: 1.5rem;
    letter-spacing: 0.3px;
}

.about p:last-child {
    margin-bottom: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
    .about {
        padding: 3rem 1.5rem;
        max-width: 100%;
    }

    .about h2 {
        font-size: 1.75rem;
    }

    .about h2 .number {
        font-size: 1.25rem;
    }

    .about p {
        font-size: 1rem;
    }
}

@media (max-width: 480px) {
    .about {
        padding: 2rem 1rem;
    }

    .about h2 {
        font-size: 1.5rem;
    }

    .about h2 .number {
        font-size: 1.1rem;
    }

    .about p {
        font-size: 0.95rem;
    }
}
</style>