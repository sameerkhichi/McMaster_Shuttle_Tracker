import map from "../images/mcmaster-parking-map.png"
import ShuttleCard from '../components/ShuttleCard';

function Home({ busLocations }) {

    return (
        <main className="p-6">
            {/* Map Image */}
            <div className="mb-8 flex justify-center">
                <img src={map} alt="McMaster Parking Map" width="800" height="600" className="rounded shadow-lg" />
            </div>
    
            {/* Shuttle Count */}
            <div className="mb-6 text-center">
                <h2 className="text-2xl font-semibold">
                Active Shuttles: {busLocations.filter(bus => bus.isRunning).length}
                </h2>
            </div>
    
            {/* Shuttle Cards */}
            <div className="flex gap-4 overflow-x-auto flex-nowrap scrollbar-hide snap-x snap-mandatory px-1 pb-4">
                {busLocations.map((bus) => (
                bus.isRunning && (
                    <ShuttleCard bus={bus} key={bus.bus_id} />
                )
                ))}
            </div>

            {/* Disclaimer Footer */}
            <footer className="text-center text-xs text-gray-500 mt-10 mb-4">
            Forgive us if we're a few minutes late - ETA varies during peak campus hours
            </footer>

        </main>
    );
}

export default Home