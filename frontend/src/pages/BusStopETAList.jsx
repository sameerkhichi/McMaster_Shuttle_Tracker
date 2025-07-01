import BusStopCard  from "../components/BusStopCard";

function addMinutesToNow(minutes) {
  const eta = new Date();
  eta.setMinutes(eta.getMinutes() + minutes);
  return eta.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function getLoopedOffset(currentIndex, targetIndex, stops) {
  const n = stops.length;
  let time = 0;
  let i = currentIndex;

  while (i !== targetIndex) {
    time += stops[i].travelTimeToNext;
    i = (i + 1) % n; // loop back to 0 if needed
  }

  return time;
}

function BusStopETAList({ busLocations }) {
    const stops = [
        { name: "MUSC", travelTimeToNext: 6 },
        { name: "A.B.B", travelTimeToNext: 2 },
        { name: "Mary Keyes", travelTimeToNext: 2 },
        { name: "Lot P", travelTimeToNext: 2 },
        { name: "Lot M", travelTimeToNext: 4 },
        { name: "Lot I", travelTimeToNext: 6 }
    ]

    return (
        <main className="flex justify-center pt-6 flex-col px-10">
            <h2 className="text-xl font-semibold text-center mb-6">Estimated Bus Times</h2>
            {
                stops.map((stop, targetIndex) => {
                    const busesAtStop = busLocations.filter(
                        bus => bus.isRunning && bus.next_stop && bus.eta != null
                    ).map(bus => {
                        const currentIndex = stops.findIndex(s => s.name === bus.next_stop);
                        if (currentIndex === -1) return null;

                        const offset = getLoopedOffset(currentIndex, targetIndex, stops);
                        const totalEta = bus.eta + offset;

                        return {
                            id: bus.bus_id,
                            totalEta,
                            arrivalTime: addMinutesToNow(totalEta)
                        };
                    })
                
                return (
                    <BusStopCard key={stop.name} stopName={stop.name} buses={busesAtStop}/>
                );
                })
            }

            {/* Disclaimer Footer */}
            <footer className="text-center text-xs text-gray-500 mt-8 mb-4">
            Please note that these times are estimated and could vary with peak campus hours
            </footer>
        </main>
    );
}

export default BusStopETAList