import bus_icon from "../images/bus-icon.png"

function ShuttleCard({bus}) {
    return (
        <div className="min-w-[300px] bg-white border border-gray-200 rounded-xl shadow-md p-4 shrink-0 snap-start">
            <img src={bus_icon} alt="Bus Icon" width="150" height="85" className="mx-auto mb-4" />
            <p><strong>Currently:</strong> {bus.nearest_stop ? `At ${bus.nearest_stop}` : `En route to ${bus.next_stop}`}</p>
            <p><strong>ETA:</strong> {bus.eta} minute(s) to {bus.next_stop}</p>
            <p><strong>Last Updated:</strong> {new Date(bus.time_stamp).toLocaleTimeString()}</p> {/*toLocaleTimeString converts the universal time to the local timezone */}
        </div>
    );
}

export default ShuttleCard