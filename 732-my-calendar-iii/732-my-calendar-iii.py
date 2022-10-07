class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        self.add_new_event((start, True))
        self.add_new_event((end, False))
        return self.count_max_overlapping()
    
    def bin_search_event(self, new_event) -> int:
        time, is_start = new_event
        l, r = 0, len(self.events)
        while l < r:
            m = (l + r) // 2
            c_time, c_is_start = self.events[m]
            if c_time < time or (c_time == time and c_is_start < is_start):
                l = m + 1
            elif c_time == time and c_is_start == is_start:
                return m
            else:
                r = m
        return r
    
    def add_new_event(self, new_event) -> None:
        index_to_insert = self.bin_search_event(new_event)
        self.events.insert(index_to_insert, new_event)
        
    def count_max_overlapping(self) -> int:
        max_active_events = 0
        nb_active_events = 0
        for _, is_start in self.events:
            if is_start:
                nb_active_events += 1
                max_active_events = max(max_active_events, nb_active_events)
            else:
                nb_active_events -= 1
        return max_active_events