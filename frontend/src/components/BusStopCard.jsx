import pin from "../images/LocationPinMcMasterTheme.png"

function BusStopCard({ stopName, buses }) {
    return (
        <div className="border rounded-xl shadow-md mb-5 pb-3 bg-white">
            <div className="bg-gray-200 rounded-t-xl flex flex-row items-center p-2">
                <img src={pin} className="w-7 pb-1" />
                <h3 className="text-xl font-bold mb-2 px-1">{stopName}</h3>
            </div>
            <div className="p-3 font-arial">
                {buses.length === 0 ? (
                    <p className="text-gray-500">No buses en route.</p>
                ) : (
                    <ul className="space-y-1">
                    {buses.map(bus => (
                        <li key={bus.id} className="text-md">
                        Bus #{bus.id} - arriving at <strong>{bus.arrivalTime}</strong> ({bus.totalEta} min)
                        </li>
                    ))}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default BusStopCard