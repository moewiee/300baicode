class Solution:
    def timeRequiredToBuy(self, tickets: list, k: int) -> int:
        current_idx = k
        ticket_to_buy = tickets[k]
        time_pass = 0
        while ticket_to_buy:
            if current_idx == 0:
                ticket_to_buy -= 1
                current_idx = len(tickets) - 1
                tickets.append(ticket_to_buy)
                tickets.pop(0)
            else:
                tickets[0] -= 1
                if tickets[0] != 0:
                    tickets.append(tickets[0])
                    tickets.pop(0)
                    current_idx -= 1
                else:
                    tickets.pop(0)
                    current_idx -= 1
            time_pass += 1
        
        return time_pass