// ========= Dinosaur Alert System =========

// Dinosaur data with locations, statuses, and special traits
const dinosaurs = [
    {
        id: 1,
        name: "T-Rex Alpha",
        species: "Tyrannosaurus Rex",
        location: "Carnivore Zone",
        status: "Active",
        lastSeen: "10 minutes ago",
        dangerLevel: 5,
        special: false,
        description: "Our main T-Rex Alpha is currently patrolling the Carnivore Zone. All visitors are advised to maintain a safe distance of at least 100 meters."
    },
    {
        id: 2,
        name: "Veloci Squad",
        species: "Velociraptors",
        location: "Raptor Valley",
        status: "Hunting",
        lastSeen: "5 minutes ago",
        dangerLevel: 4,
        special: false,
        description: "A pack of 6 Velociraptors is currently exhibiting hunting behavior. Visitors in Raptor Valley should proceed to observation decks only."
    },
    {
        id: 3,
        name: "Spike",
        species: "Stegosaurus",
        location: "Herbivore Haven",
        status: "Feeding",
        lastSeen: "2 minutes ago",
        dangerLevel: 2,
        special: false,
        description: "Our peaceful Stegosaurus is currently feeding in the Herbivore Haven. This is an excellent time for the Herbivore Tour with Feeding experience."
    },
    {
        id: 4,
        name: "Fluffy",
        species: "Therizinosaurus",
        location: "Claw Exhibit",
        status: "Sleeping",
        lastSeen: "30 minutes ago",
        dangerLevel: 3,
        special: false,
        description: "The 'Edward Scissorhands' of dinosaurs is currently resting. Despite its fearsome claws, Fluffy is a herbivore but can be territorial when awakened."
    },
    {
        id: 5,
        name: "Neon",
        species: "Bioluminescent Parasaurolophus",
        location: "Night Exhibit",
        status: "Performing",
        lastSeen: "Just now",
        dangerLevel: 1,
        special: true,
        description: "Our genetically modified Parasaurolophus with bioluminescent skin is currently performing its musical and light show in the Night Exhibit. A true park exclusive you won't see anywhere else!"
    }
];

// Function to generate a random alert
function generateRandomAlert() {
    // Pick a random dinosaur
    const randomIndex = Math.floor(Math.random() * dinosaurs.length);
    const dino = dinosaurs[randomIndex];
    
    // Update last seen time
    const minutes = Math.floor(Math.random() * 30);
    dino.lastSeen = minutes === 0 ? "Just now" : `${minutes} minutes ago`;
    
    // Randomly change status
    const statuses = ["Active", "Hunting", "Feeding", "Sleeping", "Performing", "Roaming", "Agitated"];
    dino.status = statuses[Math.floor(Math.random() * statuses.length)];
    
    // Generate alert message
    let alertClass = "info";
    if (dino.dangerLevel >= 4) {
        alertClass = "danger";
    } else if (dino.dangerLevel >= 2) {
        alertClass = "warning";
    }
    
    const alertHTML = `
        <div class="dino-alert ${alertClass}">
            <h4>${dino.name} (${dino.species})</h4>
            <p><strong>Location:</strong> ${dino.location}</p>
            <p><strong>Status:</strong> ${dino.status}</p>
            <p><strong>Last Seen:</strong> ${dino.lastSeen}</p>
            <p>${dino.description}</p>
            ${dino.special ? '<span class="special-badge">SPECIAL ATTRACTION</span>' : ''}
        </div>
    `;
    
    const alertContainer = document.getElementById("dino-alerts-container");
    
    // Create a new alert element
    const alertElement = document.createElement("div");
    alertElement.innerHTML = alertHTML;
    alertElement.classList.add("alert-item");
    
    // Add the alert to the container (at the beginning)
    alertContainer.prepend(alertElement);
    
    // Keep only the 3 most recent alerts
    const alerts = alertContainer.getElementsByClassName("alert-item");
    if (alerts.length > 3) {
        alertContainer.removeChild(alerts[alerts.length - 1]);
    }
}

// ========= Interactive Park Map =========

// Map zones with clickable areas
const mapZones = [
    {
        id: "carnivore-zone",
        name: "Carnivore Zone",
        coords: "120,150,220,250",
        shape: "rect",
        description: "Home to our fearsome T-Rex and other carnivorous dinosaurs. VIP access required for feeding shows."
    },
    {
        id: "raptor-valley",
        name: "Raptor Valley",
        coords: "250,100,350,180",
        shape: "rect",
        description: "Experience the intelligence and speed of our Velociraptor pack from secure viewing platforms."
    },
    {
        id: "herbivore-haven",
        name: "Herbivore Haven",
        coords: "380,200,480,280",
        shape: "rect",
        description: "A peaceful area where you can observe our gentle giants like Stegosaurus and Brachiosaurus."
    },
    {
        id: "claw-exhibit",
        name: "Claw Exhibit",
        coords: "300,300,380,380",
        shape: "rect",
        description: "Marvel at the impressive claws of our Therizinosaurus and other unique dinosaur adaptations."
    },
    {
        id: "night-exhibit",
        name: "Night Exhibit",
        coords: "150,350,250,450",
        shape: "circle",
        description: "Our special darkened dome where you can witness our bioluminescent Parasaurolophus perform its spectacular light show."
    },
    {
        id: "visitor-center",
        name: "Visitor Center",
        coords: "250,250,30",
        shape: "circle",
        description: "Main hub for information, dining, shopping, and emergency services. All tours start from here."
    }
];

// Function to initialize the interactive map
function initializeMap() {
    const mapContainer = document.getElementById("park-map-container");
    const mapInfo = document.getElementById("map-info");
    
    // Create the image map
    const mapHTML = `
        <img src="assets/ParkMap.png" alt="Jurasstina-Kalle Park Map" id="park-map-image" usemap="#park-map">
        <map name="park-map">
            ${mapZones.map(zone => 
                `<area shape="${zone.shape}" coords="${zone.coords}" alt="${zone.name}" 
                    data-zone="${zone.id}" href="#" title="${zone.name}">`
            ).join('')}
        </map>
    `;
    
    mapContainer.innerHTML = mapHTML;
    
    // Add event listeners to map areas
    document.querySelectorAll('map[name="park-map"] area').forEach(area => {
        area.addEventListener('click', function(e) {
            e.preventDefault();
            const zoneId = this.getAttribute('data-zone');
            const zoneData = mapZones.find(zone => zone.id === zoneId);
            
            if (zoneData) {
                mapInfo.innerHTML = `
                    <h3>${zoneData.name}</h3>
                    <p>${zoneData.description}</p>
                    <div class="zone-dinosaurs">
                        <h4>Dinosaurs in this area:</h4>
                        <ul>
                            ${dinosaurs.filter(dino => dino.location === zoneData.name)
                                .map(dino => `<li>${dino.name} - ${dino.status}</li>`)
                                .join('')}
                        </ul>
                    </div>
                `;
                
                // Highlight the selected zone
                highlightZone(zoneId);
            }
        });
        
        // Show tooltip on hover
        area.addEventListener('mouseover', function() {
            const zoneId = this.getAttribute('data-zone');
            const zoneData = mapZones.find(zone => zone.id === zoneId);
            if (zoneData) {
                this.setAttribute('title', zoneData.name);
            }
        });
    });
}

// Function to highlight the selected zone
function highlightZone(zoneId) {
    // Reset all highlights
    document.querySelectorAll('.map-highlight').forEach(el => el.remove());
    
    // Get the coordinates of the zone
    const zone = mapZones.find(z => z.id === zoneId);
    if (!zone) return;
    
    // Create highlight element based on shape
    const mapImage = document.getElementById('park-map-image');
    const mapRect = mapImage.getBoundingClientRect();
    
    const highlight = document.createElement('div');
    highlight.classList.add('map-highlight');
    
    if (zone.shape === 'rect') {
        const [x1, y1, x2, y2] = zone.coords.split(',').map(Number);
        highlight.style.left = `${x1}px`;
        highlight.style.top = `${y1}px`;
        highlight.style.width = `${x2 - x1}px`;
        highlight.style.height = `${y2 - y1}px`;
        highlight.style.borderRadius = '0';
    } else if (zone.shape === 'circle') {
        const [x, y, r] = zone.coords.split(',').map(Number);
        highlight.style.left = `${x - r}px`;
        highlight.style.top = `${y - r}px`;
        highlight.style.width = `${r * 2}px`;
        highlight.style.height = `${r * 2}px`;
        highlight.style.borderRadius = '50%';
    }
    
    document.getElementById('park-map-container').appendChild(highlight);
}

// Initialize features when DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
    // Initial setup for both features
    const existingContent = document.querySelector('main');
    
    // Create Dinosaur Alert System section
    const dinoAlertSection = document.createElement('article');
    dinoAlertSection.innerHTML = `
        <section id="dino-alert-section">
            <h2>Live Dinosaur Alerts</h2>
            <p>Stay informed about dinosaur activities and locations throughout the park.</p>
            <div id="dino-alerts-container">
                <!-- Alert items will be added here -->
            </div>
        </section>
    `;
    
    // Create Interactive Park Map section
    const parkMapSection = document.createElement('article');
    parkMapSection.innerHTML = `
        <section id="park-map-section">
            <h2>Interactive Park Map</h2>
            <p>Click on different areas to learn more about our attractions and dinosaur locations.</p>
            <div class="map-container">
                <div id="park-map-container">
                    <!-- Map will be loaded here -->
                </div>
                <div id="map-info">
                    <h3>Select an area on the map</h3>
                    <p>Click on any zone to view details and current dinosaur information.</p>
                </div>
            </div>
        </section>
    `;
    
    // Add new sections to the main content
    existingContent.appendChild(dinoAlertSection);
    existingContent.appendChild(parkMapSection);
    
    // Add CSS for the new features
    const styleElement = document.createElement('style');
    styleElement.textContent = `
        /* Dinosaur Alert System Styles */
        #dino-alert-section {
            margin-top: 2em;
            padding: 1em;
            background: #1a1a1a;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }
        
        #dino-alerts-container {
            max-height: 500px;
            overflow-y: auto;
        }
        
        .dino-alert {
            margin: 1em 0;
            padding: 1em;
            border-radius: 8px;
            border-left: 4px solid;
            transition: all 0.3s ease;
        }
        
        .dino-alert:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        
        .dino-alert.info {
            background: rgba(25, 118, 210, 0.1);
            border-left-color: #1976d2;
        }
        
        .dino-alert.warning {
            background: rgba(255, 152, 0, 0.1);
            border-left-color: #ff9800;
        }
        
        .dino-alert.danger {
            background: rgba(211, 47, 47, 0.1);
            border-left-color: #d32f2f;
        }
        
        .dino-alert h4 {
            margin-top: 0;
            color: #ffd700;
        }
        
        .special-badge {
            display: inline-block;
            background: #ffd700;
            color: #151515;
            padding: 0.3em 0.8em;
            border-radius: 4px;
            font-weight: 600;
            font-size: 0.8em;
            margin-top: 0.5em;
        }
        
        /* Interactive Park Map Styles */
        #park-map-section {
            margin-top: 2em;
            padding: 1em;
            background: #1a1a1a;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }
        
        .map-container {
            display: flex;
            flex-wrap: wrap;
            gap: 2em;
            margin-top: 1em;
        }
        
        #park-map-container {
            position: relative;
            flex: 1;
            min-width: 300px;
        }
        
        #park-map-image {
            width: 100%;
            max-width: 600px;
            height: auto;
            border-radius: 8px;
            border: 2px solid #333;
        }
        
        .map-highlight {
            position: absolute;
            border: 3px solid #ffd700;
            background: rgba(255, 215, 0, 0.2);
            pointer-events: none;
            z-index: 10;
            transition: all 0.3s ease;
        }
        
        #map-info {
            flex: 1;
            min-width: 300px;
            padding: 1em;
            background: #222;
            border-radius: 8px;
            border: 1px solid #333;
        }
        
        #map-info h3 {
            margin-top: 0;
        }
        
        .zone-dinosaurs {
            margin-top: 1em;
            padding: 1em;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 6px;
        }
        
        .zone-dinosaurs ul {
            margin: 0.5em 0 0 0;
            padding-left: 1.5em;
        }
        
        @media (max-width: 768px) {
            .map-container {
                flex-direction: column;
            }
            
            #map-info, #park-map-container {
                width: 100%;
            }
        }
    `;
    
    document.head.appendChild(styleElement);
    
    // Initialize the map
    initializeMap();
    
    // Generate initial alerts
    for (let i = 0; i < 3; i++) {
        generateRandomAlert();
    }
    
    // Set up recurring alerts
    setInterval(generateRandomAlert, 60000); // New alert every minute
    
    // Add nav links for the new features
    const navList = document.querySelector('header nav ul');
    
    // Create new nav items
    const dinoAlertNavItem = document.createElement('li');
    dinoAlertNavItem.innerHTML = '<a href="#dino-alert-section">Dino Alerts</a>';
    
    const parkMapNavItem = document.createElement('li');
    parkMapNavItem.innerHTML = '<a href="#park-map-section">Park Map</a>';
    
    // Insert the new nav items before the logout item
    const logoutNav = document.getElementById('logout-nav');
    navList.insertBefore(dinoAlertNavItem, logoutNav);
    navList.insertBefore(parkMapNavItem, logoutNav);
});