<template>
    <section class="contact" id="contact">
        <h2><span class="number">04.</span> Get In Touch</h2>
        <p>
            I'm currently looking for new opportunities, my inbox is always open. Whether you have a question or just want to say hi, feel free to reach out.
        </p>
        <div class="social-links">
            <a href="mailto:your.email@example.com" class="social-icon" aria-label="Email">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
            </a>
            <a href="https://github.com/VikingVik123/" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/victor-odimmegwa/" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            </a>
            <a href="https://x.com/Realist_Vic" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Twitter">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                </svg>
            </a>
        </div>
    </section>
</template>

<style scoped>
.contact {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 4rem 3rem;
    text-align: center;
}

.contact h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: 0.5px;
}

.contact h2 .number {
    color: #00ff00;
    font-size: 1.5rem;
    font-weight: 600;
}

.contact p {
    font-size: 1.1rem;
    color: #9ca3af;
    line-height: 1.8;
    max-width: 600px;
    margin-bottom: 2.5rem;
    letter-spacing: 0.3px;
}

.social-links {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
}

.social-icon {
    width: 60px;
    height: 60px;
    border: 2px solid #333;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    transition: all 0.3s ease;
    background: #000000;
    text-decoration: none;
}

.social-icon svg {
    width: 30px;
    height: 30px;
}

.social-icon:hover {
    background: #000000;
    color: #ffffff;
    border-color: #00ff00;
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 255, 0, 0.3);
}

/* Responsive Design */
@media (max-width: 768px) {
    .contact {
        padding: 3rem 1.5rem;
    }

    .contact h2 {
        font-size: 1.75rem;
    }

    .contact h2 .number {
        font-size: 1.25rem;
    }

    .contact p {
        font-size: 1rem;
    }

    .social-icon {
        width: 60px;
        height: 60px;
    }

    .social-icon svg {
        width: 30px;
        height: 30px;
    }

    .social-icon:active {
        transform: scale(0.95);
    }
}

@media (max-width: 480px) {
    .contact {
        padding: 2rem 1rem;
    }

    .contact h2 {
        font-size: 1.5rem;
        flex-direction: column;
        gap: 0.25rem;
    }

    .contact h2 .number {
        font-size: 1.1rem;
    }

    .contact p {
        font-size: 0.95rem;
        line-height: 1.7;
    }

    .social-links {
        gap: 1rem;
    }

    .social-icon {
        width: 56px;
        height: 56px;
    }

    .social-icon svg {
        width: 28px;
        height: 28px;
    }
}
</style>