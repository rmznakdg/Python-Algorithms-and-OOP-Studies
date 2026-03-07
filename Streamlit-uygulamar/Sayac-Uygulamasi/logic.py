import time

class Counter():
    def __init__(self, count=0):
        # Manuel sayaç değişkenleri
        self.count = count
        
        # Zamanlayıcı (kronometre) değişkenleri
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
        self.laps = []

    # --- MANUEL SAYAÇ METOTLARI ---
    def starting_value(self, new_starting=0):
        self.count = new_starting
        return self.count

    def increment_counter(self, increment=1):
        self.count += increment
        return self.count

    def decrement_counter(self, decrement=1):
        self.count -= decrement
        return self.count

    def reset_counter(self):
        """Hem manuel sayacı hem de kronometreyi sıfırlar."""
        self.count = 0
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
        self.laps = []
        return self.count

    def reset_stopwatch(self):
        """Sadece kronometreyi sıfırlar."""
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
        self.laps = []

    # --- ZAMANLAYICI (KRONOMETRE) METOTLARI ---
    def start_timer(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True

    def pause_timer(self):
        if self.is_running:
            self.elapsed_time += time.time() - self.start_time
            self.is_running = False
            self.start_time = None

    def get_time(self):
        if self.is_running:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time

    def get_time_formatted(self):
        total_seconds = self.get_time()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds * 100) % 100)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

    def record_lap(self):
        if self.is_running or self.elapsed_time > 0:
            formatted_time = self.get_time_formatted()
            # Tur adını ve zamanı kaydet
            self.laps.append(formatted_time)
            return formatted_time
        return None
