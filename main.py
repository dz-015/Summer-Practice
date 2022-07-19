import calculations
from cylindrical_point import CylindricalPoint

def main():
    p1 = CylindricalPoint(0, 0, 0)
    p2 = CylindricalPoint(0, 1, 1)
    p3 = CylindricalPoint(1, 0, 1)
    print(calculations.triangle_area(
        p1.convert(),
        p2.convert(),
        p3.convert()
    ))

if __name__ == "__main__":
    main()