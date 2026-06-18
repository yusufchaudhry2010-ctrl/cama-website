with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/styles.css', 'a') as f:
    f.write('''
/* Media Page Styles */
.media-section {
  padding: 6rem 2rem;
}
.media-masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  grid-auto-rows: 250px;
  gap: 1.5rem;
}
.media-item {
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-card);
  transition: transform var(--transition), box-shadow var(--transition);
}
.media-item:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  z-index: 2;
}
.media-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}
.media-item:hover img {
  transform: scale(1.05);
}

/* Make some items span 2 rows if needed */
.media-item:nth-child(3n) {
  grid-row: span 2;
}
.media-item:nth-child(5n) {
  grid-column: span 2;
}

/* Responsive adjustments for masonry */
@media (max-width: 768px) {
  .media-masonry {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    grid-auto-rows: 200px;
  }
  .media-item:nth-child(5n) {
    grid-column: span 1;
  }
}
''')
print("CSS updated")
