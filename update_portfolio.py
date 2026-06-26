import re

# Update CSS
with open('styles/style.css', 'r') as f:
    css = f.read()

css_new = """/* Projects Stack (Parth Style) */
.projects-stack {
  display: flex;
  flex-direction: column;
  gap: 4rem;
}

.featured-project {
  display: flex;
  flex-direction: row;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 16px;
  overflow: hidden;
  transition: var(--transition);
}

.featured-project:nth-child(even) {
  flex-direction: row-reverse;
}

.featured-project:hover {
  transform: translateY(-10px);
  border-color: rgba(255,255,255,0.2);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.featured-project-img {
  flex: 1;
  position: relative;
  min-height: 300px;
}

.featured-project-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  transition: transform 0.5s;
}

.featured-project:hover .featured-project-img img {
  transform: scale(1.05);
}

.featured-project-content {
  flex: 1;
  padding: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.featured-project-title {
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.featured-project-desc {
  color: var(--text-secondary);
  font-size: 1rem;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.featured-project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.project-links {
  display: flex;
  gap: 1rem;
  margin-top: auto;
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--card-border);
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--text-primary);
  transition: var(--transition);
}

.project-link:hover {
  background: rgba(14, 165, 233, 0.2);
  border-color: var(--accent-color);
  color: var(--accent-color);
}

/* Skills (Sharath Style) */
.skills-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 16px;
  padding: 2.5rem;
}

.skill-group {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  padding-bottom: 1.5rem;
}

.skill-group:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.skill-group-title {
  min-width: 250px;
  font-weight: 600;
  font-size: 1.1rem;
  color: var(--text-primary);
}

.skill-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.chip {
  padding: 0.4rem 1rem;
  background: rgba(14, 165, 233, 0.1);
  border: 1px solid rgba(14, 165, 233, 0.2);
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--accent-color);
  transition: var(--transition);
}

.chip:hover {
  background: var(--accent-color);
  color: #fff;
}

@media (max-width: 900px) {
  .featured-project, .featured-project:nth-child(even) {
    flex-direction: column;
  }
  .featured-project-img {
    min-height: 250px;
  }
  .skill-group {
    flex-direction: column;
    gap: 0.5rem;
  }
  .skill-group-title {
    min-width: auto;
  }
}
"""

css_regex = re.compile(r'/\* Projects Grid \*/.*?\.skill-tag:hover \{[^}]*\}\s*\}?', re.DOTALL)
css_updated = css_regex.sub(css_new, css)

with open('styles/style.css', 'w') as f:
    f.write(css_updated)

# Update HTML
with open('index.html', 'r') as f:
    html = f.read()

html_new = """      <div class="projects-stack">

        <!-- Project 1 -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/amr_human_detection.png" alt="AMR Human Detection">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Human Detection for Autonomous Mobile Robots</h3>
            <p class="featured-project-desc">A real-time AI pipeline for human detection on AMRs using LIDAR occupancy maps, U-Net, YOLOv5, and camera/LIDAR sensor fusion, improving indoor logistics safety.</p>
            <div class="featured-project-tech">
              <span class="tech-tag">LIDAR</span>
              <span class="tech-tag">U-Net</span>
              <span class="tech-tag">YOLOv5</span>
              <span class="tech-tag">Sensor Fusion</span>
            </div>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/dynamic_geofence.png" alt="Dynamic Geofence">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Dynamic Geofence for Autonomous Mobile Robots</h3>
            <p class="featured-project-desc">Built a real-time safety application using computational geometry to dynamically visualize risk zones, supporting safer robot navigation in indoor environments.</p>
            <div class="featured-project-tech">
              <span class="tech-tag">Vue.js</span>
              <span class="tech-tag">Flask</span>
              <span class="tech-tag">MQTT</span>
              <span class="tech-tag">SQLite</span>
            </div>
            <div class="project-links">
              <a href="https://github.com/SowjanyaKrishna/Dynamic-Geofence-for-Autonomous-Mobile-Robots-AMR-in-Indoor-Logistics" target="_blank" class="project-link">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg> GitHub
              </a>
            </div>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/smart_farming.png" alt="Smart Farming">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Smart Farming using HVAC and IoT</h3>
            <p class="featured-project-desc">An IoT automation prototype using Raspberry Pi, MQTT, sensor integration, and a PDDL planner for automated decision-making and HVAC-related control.</p>
            <div class="featured-project-tech">
              <span class="tech-tag">Raspberry Pi</span>
              <span class="tech-tag">MQTT</span>
              <span class="tech-tag">Dash</span>
              <span class="tech-tag">PDDL</span>
            </div>
            <div class="project-links">
              <a href="https://github.com/SowjanyaKrishna/Smart-Farming-using-HVAC-and-IoT" target="_blank" class="project-link">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg> GitHub
              </a>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="container">
      <h2>Technical Skills</h2>
      <div class="skills-wrapper fade-in">

        <div class="skill-group">
          <div class="skill-group-title">Software Development & Backend</div>
          <div class="skill-chips">
            <span class="chip">Python</span>
            <span class="chip">Flask</span>
            <span class="chip">REST APIs</span>
            <span class="chip">JSON</span>
            <span class="chip">JavaScript</span>
            <span class="chip">SQL</span>
            <span class="chip">Git</span>
            <span class="chip">CI/CD</span>
            <span class="chip">Shell Scripting</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Frontend & Applications</div>
          <div class="skill-chips">
            <span class="chip">React</span>
            <span class="chip">Next.js</span>
            <span class="chip">Vue.js</span>
            <span class="chip">PyQt</span>
            <span class="chip">Grafana</span>
            <span class="chip">Power BI</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Cloud & Deployment</div>
          <div class="skill-chips">
            <span class="chip">Microsoft Azure</span>
            <span class="chip">Docker</span>
            <span class="chip">Linux</span>
            <span class="chip">VM Deployment</span>
            <span class="chip">MongoDB</span>
            <span class="chip">InfluxDB</span>
            <span class="chip">Terraform</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Data & AI Pipelines</div>
          <div class="skill-chips">
            <span class="chip">ML-ready Datasets</span>
            <span class="chip">ETL/ELT Workflows</span>
            <span class="chip">Telegraf</span>
            <span class="chip">Data Architecture</span>
            <span class="chip">Time-Series</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">IT/OT Integration</div>
          <div class="skill-chips">
            <span class="chip">Siemens S7</span>
            <span class="chip">Beckhoff TwinCAT</span>
            <span class="chip">OPC UA</span>
            <span class="chip">MQTT</span>
            <span class="chip">SmartUnifier</span>
            <span class="chip">Edge-PC</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Industrial IoT</div>
          <div class="skill-chips">
            <span class="chip">Raspberry Pi</span>
            <span class="chip">5G/IIoT</span>
            <span class="chip">Sensor Data Workflows</span>
            <span class="chip">Cloud-connected IoT</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Digital Twin & Standards</div>
          <div class="skill-chips">
            <span class="chip">Asset Administration Shell (AAS)</span>
            <span class="chip">BaSyx</span>
            <span class="chip">FA3ST</span>
            <span class="chip">IDTA Submodels</span>
            <span class="chip">Digital Twin Data Models</span>
          </div>
        </div>

        <div class="skill-group">
          <div class="skill-group-title">Data Spaces & Interoperability</div>
          <div class="skill-chips">
            <span class="chip">Eclipse Dataspace Connector (EDC)</span>
            <span class="chip">Manufacturing-X</span>
            <span class="chip">Catena-X</span>
          </div>
        </div>

      </div>"""

html_regex = re.compile(r'<div class="projects-grid">.*?</section>\s*<!-- Publications & Education -->', re.DOTALL)
html_updated = html_regex.sub(html_new + '\n    </section>\n\n    <!-- Publications & Education -->', html)

with open('index.html', 'w') as f:
    f.write(html_updated)

