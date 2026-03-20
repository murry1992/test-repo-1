import React from "react";
import { kpiData, dailySeries } from "./mockData";

export const App: React.FC = () => {
  return (
    <div className="page">
      <header className="header">
        <h1>Stock Market KPIs</h1>
        <p className="subtitle">Mock data for the past 7 trading days</p>
      </header>

      <main className="content">
        <section className="kpi-grid">
          {kpiData.map((kpi) => (
            <article key={kpi.label} className="kpi-card">
              <div className="kpi-label">{kpi.label}</div>
              <div className="kpi-value">{kpi.value}</div>
              <div
                className={
                  "kpi-change " + (kpi.change >= 0 ? "kpi-change-up" : "kpi-change-down")
                }
              >
                {kpi.change >= 0 ? "+" : ""}
                {kpi.change.toFixed(2)}%
              </div>
              <div className="kpi-caption">{kpi.caption}</div>
            </article>
          ))}
        </section>

        <section className="chart-card">
          <div className="chart-header">
            <h2>Index Close (Last 7 Days)</h2>
            <span className="chart-subtitle">Mock S&P 500 style index</span>
          </div>
          <MiniLineChart data={dailySeries} />
        </section>
      </main>
    </div>
  );
};

type Point = { label: string; value: number };

interface MiniLineChartProps {
  data: Point[];
}

const MiniLineChart: React.FC<MiniLineChartProps> = ({ data }) => {
  const padding = 20;
  const width = 640;
  const height = 260;

  const values = data.map((d) => d.value);
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;

  const xStep = (width - padding * 2) / (data.length - 1 || 1);

  const points = data
    .map((d, i) => {
      const x = padding + i * xStep;
      const y = padding + ((max - d.value) / range) * (height - padding * 2);
      return `${x},${y}`;
    })
    .join(" ");

  const last = data[data.length - 1];

  return (
    <svg
      className="chart"
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label="Mock stock index over the past week"
    >
      <defs>
        <linearGradient id="areaGradient" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#22c55e" stopOpacity="0.4" />
          <stop offset="100%" stopColor="#22c55e" stopOpacity="0" />
        </linearGradient>
      </defs>

      <polyline
        fill="none"
        stroke="#e5e7eb"
        strokeWidth="1"
        points={`${padding},${height - padding} ${width - padding},${
          height - padding
        }`}
      />

      <polyline
        fill="none"
        stroke="#4b5563"
        strokeWidth="1"
        points={`${padding},${padding} ${padding},${height - padding}`}
      />

      <polyline
        fill="url(#areaGradient)"
        stroke="none"
        points={`${padding},${height - padding} ${points} ${
          width - padding
        },${height - padding}`}
      />

      <polyline
        fill="none"
        stroke="#22c55e"
        strokeWidth="2.5"
        strokeLinejoin="round"
        strokeLinecap="round"
        points={points}
      />

      {data.map((d, i) => {
        const x = padding + i * xStep;
        const y = padding + ((max - d.value) / range) * (height - padding * 2);
        return (
          <circle
            key={d.label}
            cx={x}
            cy={y}
            r={i === data.length - 1 ? 4 : 3}
            className="chart-dot"
          />
        );
      })}

      <text
        x={width - padding}
        y={padding + 4}
        textAnchor="end"
        className="chart-label"
      >
        Last close: {last.value.toFixed(2)}
      </text>
      <text
        x={width - padding}
        y={padding + 22}
        textAnchor="end"
        className="chart-label-muted"
      >
        {last.label}
      </text>
    </svg>
  );
};
