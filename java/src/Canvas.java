
import javax.swing.JComponent;
import java.awt.*;
import java.awt.geom.*;

import java.util.ArrayList;

public class Canvas extends JComponent {
    int circleSize;
    boolean line;

    static ArrayList<Point> pointsArray = new ArrayList<>();
    static ArrayList<Boolean> drawPointArray = new ArrayList<>();

    Canvas(int circleSize, boolean line) {
        this.circleSize = circleSize;
        this.line = line;
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        RenderingHints hints = new RenderingHints(
            RenderingHints.KEY_ANTIALIASING,
            RenderingHints.VALUE_ANTIALIAS_ON
        );
        g2d.addRenderingHints(hints);

        g2d.setColor(Color.BLACK);

        Point point;        
        Point prev = null;

        for (int i = 0; i < pointsArray.size(); i++) {    
            point = pointsArray.get(i);   

            if (drawPointArray.get(i)) {
                drawPoint(g2d, point);
            }
            
            if (prev != null && line) {
                drawLine(g2d, point, prev);
            }

            prev = point;
        }
    }

    private void drawLine(Graphics2D g2d, Point point, Point prev) {
        Line2D.Double line = new Line2D.Double(
            point.getX() + circleSize / 2,
            point.getY() + circleSize / 2,
            prev.getX() + circleSize / 2, 
            prev.getY() + circleSize / 2
        );
        g2d.draw(line);
    }

    private void drawPoint(Graphics2D g2d, Point point) {
        // Rectangle2D.Double circle = new Rectangle2D.Double(
        Ellipse2D.Double circle = new Ellipse2D.Double(
            point.getX(),
            point.getY(),
            circleSize,
            circleSize
        );
        g2d.fill(circle);
    }
}
