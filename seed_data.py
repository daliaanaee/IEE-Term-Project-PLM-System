from sqlmodel import SQLModel, create_engine, Session
from models import Team, Design, TeamDesign, Chassis
from datetime import datetime

sqlite_url = "sqlite:///term_project.db"
engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    # Add teams
    session.add_all([
        Team(TeamName="Red Robots"),
        Team(TeamName="Orange Ocelots"),
        Team(TeamName="Green Goblins"),
        Team(TeamName="Blue Jackals")
    ])

    # Add designs
    session.add_all([
        Design(DesignID=1, CodeName="tennis bakerloo", ChassisType="B", UnitCost=35, UnitRevenue=111),
        Design(DesignID=2, CodeName="floor california", ChassisType="A", UnitCost=27, UnitRevenue=106)
    ])

    # Link teams to designs
    session.add_all([
        TeamDesign(TeamName="Red Robots", DesignID=1),
        TeamDesign(TeamName="Orange Ocelots", DesignID=2),
        TeamDesign(TeamName="Green Goblins", DesignID=1),
        TeamDesign(TeamName="Blue Jackals", DesignID=2)
    ])

    # Add chassis records
    session.add_all([
        Chassis(
            Serial="A333",
            TeamName="Blue Jackals",
            PurchaseTimestamp=datetime(2024, 7, 24, 15, 28, 16),
            SaleTimestamp=datetime(2024, 7, 24, 15, 29, 17),
            Status="Sold"
        ),
        Chassis(
            Serial="A209",
            TeamName="Blue Jackals",
            PurchaseTimestamp=datetime(2024, 7, 24, 15, 28, 59),
            SaleTimestamp=None,
            Status="Purchased"
        ),
        Chassis(
            Serial="A105",
            TeamName="Orange Ocelots",
            PurchaseTimestamp=datetime(2024, 7, 24, 15, 28, 51),
            SaleTimestamp=datetime(2024, 7, 24, 15, 30, 9),
            Status="Sold"
        )
    ])

    session.commit()
