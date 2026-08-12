import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const responseData = [
  { time: "10:00", response: 120 },
  { time: "10:05", response: 145 },
  { time: "10:10", response: 132 },
  { time: "10:15", response: 168 },
  { time: "10:20", response: 141 },
  { time: "10:25", response: 155 },
  { time: "10:30", response: 128 },
];

export default function ResponseChart() {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-gray-900">
          Response Time
        </h2>

        <p className="mt-1 text-sm text-gray-500">
          Average service response time over recent checks.
        </p>
      </div>

      <div className="h-[320px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={responseData}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="time"
              tick={{ fontSize: 12 }}
            />

            <YAxis
              unit="ms"
              tick={{ fontSize: 12 }}
            />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="response"
              stroke="#2563eb"
              strokeWidth={3}
              dot={{ r: 4 }}
              activeDot={{ r: 6 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
