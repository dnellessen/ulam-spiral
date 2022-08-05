
import java.awt.Point;
import javax.swing.JFrame;

public class UlamSpiral {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;

    private static int circleSize = 2;
    private static boolean line = false;

    private static int xFactor;
    private static int yFactor;

    public static void main(String[] args) {
        if (args.length == 1) {
            circleSize = Integer.parseInt(args[0]);
        } else if (args.length == 2) {
            circleSize = Integer.parseInt(args[0]);
            line = Boolean.parseBoolean(args[1]);
        }

        createFrame();
    }

    private static void createFrame() {
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(circleSize, line);

        frame.setSize(WIDTH, HEIGHT);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        addPoints();
        frame.add(canvas);

        frame.setVisible(true);
    }

    private static void addPoints() {
        int num = 1;
        int x = WIDTH / 2 - circleSize / 2;
        int y = HEIGHT / 2 - circleSize / 2;
        char direction = changeDirection('s'); // -> e
        int steps = 1;
        int stepsTaken = 0;
        boolean directionChanged = false;

        while (x < WIDTH) {
            Canvas.pointsArray.add(new Point(x, y));
            Canvas.drawPointArray.add(isPrime(num));

            if (stepsTaken == steps) {
                direction = changeDirection(direction);

                if (directionChanged) {
                    steps++;
                    directionChanged = false;
                } else {
                    directionChanged = true;
                }
                stepsTaken = 0;
            }

            x += xFactor;
            y += yFactor;
            
            stepsTaken++;
            num++;
        }
    }

    private static char changeDirection(char direction) {
        switch (direction) {
            case 'n':
                direction = 'w';
                yFactor = 0;
                xFactor = -circleSize;
                break;
            case 'w':
                direction = 's';
                yFactor = circleSize;
                xFactor = 0;
                break;
            case 's':
                direction = 'e';
                yFactor = 0;
                xFactor = circleSize;
                break;
            case 'e':
                direction = 'n';
                yFactor = -circleSize;
                xFactor = 0;
                break;
        }
        return direction;
    }

    private static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }

        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

}
