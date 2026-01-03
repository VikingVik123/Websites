<script setup>

</script>

<template>
    <section class="tech" id="techstack">
        <h2><span class="number">02.</span> Tech Stack</h2>
        <div class="tech-grid">
            <div class="tech-category">
                <h3>LANGUAGES</h3>
                <ul>
                    <li>Python</li> 
                    <li>JavaScript</li>
                </ul>
            </div>
            <div class="tech-category">
                <h3>FRAMEWORKS</h3>
                <ul>
                    <li>FastAPI</li> 
                    <li>Django</li>
                    <li>Flask</li>
                    <li>Express.js</li>
                </ul>
            </div>
            <div class="tech-category">
                <h3>DATABASES</h3>
                <ul>
                    <li>PostgreSQL</li> 
                    <li>MongoDB</li>
                    <li>Redis</li>
                    <li>MySQL</li>
                </ul>
            </div>
            <div class="tech-category">
                <h3>INFRASTRUCTURE</h3>
                <ul>
                    <li>AWS</li> 
                    <li>Docker</li>
                    <li>GCP</li>
                </ul>
            </div>
            <div class="tech-category">
                <h3>TOOLS</h3>
                <ul>
                    <li>gRPC</li> 
                    <li>RabbitMQ</li>
                    <li>GraphQL</li>
                </ul>
            </div>
        </div>
    </section>
</template>

<style scoped>
.tech {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 3rem;
}

.tech h2 {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 3rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: 0.5px;
}

.tech h2 .number {
    color: var(--accent-green);
    font-size: 1.5rem;
    font-weight: 600;
}

.tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1200px;
}

.tech-category {
    background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
    border: 2px solid var(--border-primary);
    padding: 1.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.tech-category:hover {
    border-color: var(--accent-green);
    transform: translateY(-4px);
    box-shadow: 0 8px 24px var(--green-glow-light);
}

.tech-category h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--accent-green);
    margin-bottom: 1rem;
    letter-spacing: 1px;
}

.tech-category ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 0.5rem;
}

.tech-category li {
    background: var(--bg-secondary);
    border: 1px solid var(--border-secondary);
    padding: 0.5rem 0.75rem;
    border-radius: 4px;
    color: var(--text-tertiary);
    font-size: 0.9rem;
    transition: all 0.3s ease;
    cursor: default;
    text-align: center;
}

.tech-category li:hover {
    background: var(--bg-gradient-end);
    border-color: var(--accent-green);
    color: var(--text-secondary);
    transform: translateY(-2px);
}

/* Responsive Design */
@media (max-width: 768px) {
    .tech {
        padding: 3rem 1.5rem;
    }

    .tech h2 {
        font-size: 1.75rem;
    }

    .tech h2 .number {
        font-size: 1.25rem;
    }

    .tech-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }

    .tech-category ul {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .tech {
        padding: 2rem 1rem;
    }

    .tech h2 {
        font-size: 1.5rem;
    }

    .tech h2 .number {
        font-size: 1.1rem;
    }

    .tech-category {
        padding: 1.25rem;
    }

    .tech-category h3 {
        font-size: 0.9rem;
    }

    .tech-category ul {
        grid-template-columns: 1fr;
        gap: 0.5rem;
    }

    .tech-category li {
        padding: 0.6rem 0.75rem;
        font-size: 0.85rem;
    }
}
</style>

