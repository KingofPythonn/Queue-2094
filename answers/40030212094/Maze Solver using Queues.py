from Queue import Queue


class MazeSolver:
    def __init__(self,maze):
        self.maze=maze
        self.rows=len(maze)
        self.cols=len(maze[0])
        self.start=None
        self.end=None
        
        for i in range(self.rows):
            for j in range(self.cols):
                if maze[i][j]=='S':
                    self.start=(i,j)
                elif maze[i][j]=='E':
                    self.end=(i,j)

    def move_valiation(self,row,col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == '0'
   

    def find_shortest_path(self):
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

       
        queue = Queue()
        queue.enqueue((self.start, 0)) 
        visited = set()

     
        while not queue.is_empty():
            (row, col), distance = queue.dequeue()

         
            if (row, col) == self.end:
                return distance

            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

               
                if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                    queue.enqueue(((new_row, new_col), distance + 1))
                    visited.add((new_row, new_col))

        
        return -1


