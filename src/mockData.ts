export interface Kpi {
  label: string;
  value: string;
  change: number;
  caption: string;
}

export interface DailyPoint {
  label: string;
  value: number;
}

export const kpiData: Kpi[] = [
  {
    label: "Index Level",
    value: "4,520.67",
    change: 1.24,
    caption: "vs. last week close"
  },
  {
    label: "Weekly Return",
    value: "+1.8%",
    change: 1.8,
    caption: "price-only performance"
  },
  {
    label: "Best Day",
    value: "+0.9%",
    change: 0.9,
    caption: "Thursday intraday rally"
  },
  {
    label: "Worst Day",
    value: "-0.6%",
    change: -0.6,
    caption: "Monday opening weakness"
  }
];

export const dailySeries: DailyPoint[] = [
  { label: "Mon", value: 4468.12 },
  { label: "Tue", value: 4482.45 },
  { label: "Wed", value: 4510.33 },
  { label: "Thu", value: 4530.91 },
  { label: "Fri", value: 4524.7 },
  { label: "Mon", value: 4518.21 },
  { label: "Tue", value: 4520.67 }
];
