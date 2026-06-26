import re

html_new = """      <div class="projects-stack">

        <!-- Project 1 (Fraunhofer) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/digibattpro.png" alt="DigiBattPro">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">DigiBattPro 4.0 - Dynamic PCF & Battery Passport</h3>
            <div class="featured-project-desc">
              <p>Implemented digital twin use cases connecting battery production data, dynamic Product Carbon Footprint (PCF) calculation, and data-space concepts.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Bridging raw clean-room energy sensor data with standardized PCF calculation logic and creating a traceable Digital Battery Passport.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Built a data acquisition pipeline utilizing Xetics triggers and InfluxDB, integrated with AAS submodels and the FA3ST service repository.</li>
                <li><strong>Results:</strong> Successfully connected dynamic production data with PCF environmental assessment, establishing a structured MVP for a searchable, interoperable Digital Battery Passport.</li>
              </ul>
            </div>
            <div class="featured-project-tech">
              <span class="tech-tag">Asset Administration Shell</span>
              <span class="tech-tag">FA3ST</span>
              <span class="tech-tag">Xetics</span>
              <span class="tech-tag">InfluxDB</span>
              <span class="tech-tag">Python</span>
            </div>
          </div>
        </div>

        <!-- Project 2 (Fraunhofer) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/ki_data_platform.png" alt="KI Data Platform">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">KI Data Platform - AAS & DCAT-AP Harvester</h3>
            <div class="featured-project-desc">
              <p>Developed workflows for an AI data platform to give manufacturing companies secure, structured access to production data spaces.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Transforming highly complex, industrial Asset Administration Shell (AAS) models into discoverable datasets for modern metadata catalogues like Piveau.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Built an AAS-to-DCAT harvester workflow that queries FA3ST AAS registries, dynamically maps them to DCAT-AP/JRC-compatible metadata, and publishes them.</li>
                <li><strong>Results:</strong> Successfully demonstrated the end-to-end AAS upload to the data platform for industry partners, enabling seamless data discoverability for Manufacturing-X.</li>
              </ul>
            </div>
            <div class="featured-project-tech">
              <span class="tech-tag">Piveau</span>
              <span class="tech-tag">DCAT-AP</span>
              <span class="tech-tag">AAS Registry</span>
              <span class="tech-tag">REST APIs</span>
              <span class="tech-tag">Keycloak</span>
            </div>
          </div>
        </div>

        <!-- Project 3 (Fraunhofer) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/exelpro.png" alt="ExELPro">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">ExELPro - AI-supported Experiment Management</h3>
            <div class="featured-project-desc">
              <p>Developed an intelligent Experiment Management System (EMS) pipeline for optimizing complex battery cell production processes.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Collecting disparate process data from mixing, coating, and assembly stages and converting it into machine-learning-ready training data.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Engineered an end-to-end pipeline connecting SmartUnifier, Edge-PCs, OPC UA, MQTT, and InfluxDB to cloud-based ML services and the EMS.</li>
                <li><strong>Results:</strong> Shifted the EMS from a pure analysis tool to an intelligent assistance system, using ML to predict process parameters (e.g. target viscosity) and drastically reduce iterative physical tests.</li>
              </ul>
            </div>
            <div class="featured-project-tech">
              <span class="tech-tag">SmartUnifier</span>
              <span class="tech-tag">InfluxDB</span>
              <span class="tech-tag">OPC UA / MQTT</span>
              <span class="tech-tag">Edge-PC</span>
              <span class="tech-tag">Telegraf</span>
            </div>
          </div>
        </div>

        <!-- Project 4 (Academic) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/amr_human_detection.png" alt="AMR Human Detection">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Human Detection for Autonomous Mobile Robots</h3>
            <div class="featured-project-desc">
              <p>Conducted in-depth research to build a real-time AI pipeline for human detection on AMRs in complex indoor logistics environments.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Accurate human leg detection and tracking using noisy LIDAR point clouds while maintaining strict real-time performance.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Adapted a U-Net architecture specifically for LIDAR occupancy map images and utilized YOLOv5 on camera data for robust human classification.</li>
                <li><strong>Results:</strong> Implemented a successful multi-sensor fusion approach. Developed a robust system to calculate the mass center directly from occupancy maps, enabling highly accurate localization.</li>
              </ul>
            </div>
            <div class="featured-project-tech">
              <span class="tech-tag">LIDAR</span>
              <span class="tech-tag">U-Net</span>
              <span class="tech-tag">YOLOv5</span>
              <span class="tech-tag">Sensor Fusion</span>
            </div>
          </div>
        </div>

        <!-- Project 5 (Academic) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/dynamic_geofence.png" alt="Dynamic Geofence">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Dynamic Geofence for Autonomous Mobile Robots</h3>
            <div class="featured-project-desc">
              <p>Designed a real-time safety application to manage dynamic risk zones for AMRs operating in shared indoor industrial environments.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Managing concurrent data streams from multiple AMRs without lag, and dynamically rendering reliable safety boundaries on the fly.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Developed a novel approach based on computational geometry. Built a monitoring application using Vue.js, Flask, MQTT, and SQLite.</li>
                <li><strong>Results:</strong> Overcame concurrency issues by implementing a real-time caching system using thread-safe data structures, establishing a verifiable safety case for AMR operations.</li>
              </ul>
            </div>
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

        <!-- Project 6 (Academic) -->
        <div class="featured-project fade-in">
          <div class="featured-project-img">
            <img src="assets/img/smart_farming.png" alt="Smart Farming">
          </div>
          <div class="featured-project-content">
            <h3 class="featured-project-title">Smart Farming using HVAC and IoT</h3>
            <div class="featured-project-desc">
              <p>Created an end-to-end IoT automation prototype designed to modernize environmental control in farming scenarios.</p>
              <ul>
                <li style="margin-bottom: 0.5rem"><strong>The Challenge:</strong> Reliably transmitting data from distributed sensors and translating that raw data into automated, intelligent HVAC control decisions.</li>
                <li style="margin-bottom: 0.5rem"><strong>The Solution:</strong> Integrated multiple sensors connected to a Raspberry Pi, leveraging MQTT for robust data transfer. Engineered an interactive Dash web application.</li>
                <li><strong>Results:</strong> Successfully implemented a PDDL AI planner that autonomously evaluated sensor inputs to make smart decision-making protocols and drive actuator control.</li>
              </ul>
            </div>
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

      </div>"""

with open('index.html', 'r') as f:
    html = f.read()

html_regex = re.compile(r'<div class="projects-stack">.*?</section>\s*<!-- Skills Section -->', re.DOTALL)
html_updated = html_regex.sub(html_new + '\n    </section>\n\n    <!-- Skills Section -->', html)

with open('index.html', 'w') as f:
    f.write(html_updated)

