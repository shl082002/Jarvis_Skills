import { NavLink, Outlet } from "react-router-dom";
import { HiOutlineMap, HiOutlineQueueList, HiOutlineServer } from "react-icons/hi2";
import { INK, MIX, OCCASION_RAIL } from "../lib/ink";
import { MorningSwitch } from "./MorningSwitch";
import { ModeSwitch } from "./ModeSwitch";
import { GauntletSwitch } from "./GauntletSwitch";
import type { CockpitState } from "../types";

const NAV = [
  { to: "/", label: "Board", icon: HiOutlineMap, end: true },
  { to: "/runs", label: "Runs", icon: HiOutlineQueueList, end: false },
  { to: "/services", label: "Services", icon: HiOutlineServer, end: false },
] as const;

export function Shell({ state }: { state: CockpitState }) {
  const occasion = state.occasion ?? "deep";
  const rail = OCCASION_RAIL[occasion] ?? OCCASION_RAIL.deep;
  return (
    <div className="flex h-[100dvh] w-[100vw] overflow-hidden bg-[#0b0e14]">
      <aside className={`w-[0.35rem] shrink-0 ${rail}`} aria-hidden />
      <div className="flex min-w-0 flex-1 flex-col">
        <header className="sticky top-0 z-20 flex h-[12vh] shrink-0 items-center justify-between gap-[1.2vw] border-b border-[#243044]/80 bg-[#0b0e14]/85 px-[2vw] backdrop-blur-md">
          <div className="min-w-0">
            <h1 className="truncate font-semibold tracking-[0.12em] text-[clamp(1.1rem,2.4vh,1.85rem)] uppercase">
              Jarvis Mission Control
            </h1>
            <p className={`hidden text-[0.65rem] uppercase tracking-wider sm:block ${INK.mute}`}>
              {occasion} · {MIX[occasion] ?? MIX.away}
            </p>
          </div>
          <nav className="hidden items-center gap-[0.4vw] md:flex">
            {NAV.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.end}
                className={({ isActive }) =>
                  `flex items-center gap-[0.4vw] rounded-full px-[0.9vw] py-[0.6vh] text-[0.7rem] uppercase tracking-wider ${
                    isActive ? "bg-[#1a2233] text-[#e8edf7]" : `${INK.mute} hover:text-[#e8edf7]`
                  }`
                }
              >
                <item.icon className="h-[1rem] w-[1rem]" />
                {item.label}
              </NavLink>
            ))}
          </nav>
          <div className="flex shrink-0 items-center gap-[1vw]">
            <span className={`hidden text-[0.65rem] uppercase tracking-wider lg:inline ${INK.mute}`}>
              {state.mode}
            </span>
            <MorningSwitch
              on={Boolean(state.morning_open?.on)}
              hour={state.morning_open?.hour ?? 6}
              minute={state.morning_open?.minute ?? 0}
              errText={state.morning_open?.last_error}
            />
            <GauntletSwitch on={Boolean(state.gauntlet?.on)} />
            <ModeSwitch current={state.mode} />
          </div>
        </header>
        <nav className="flex h-[6vh] items-center gap-[1vw] border-b border-[#243044]/60 px-[2vw] md:hidden">
          {NAV.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) =>
                `flex items-center gap-[0.4vw] text-[0.7rem] uppercase tracking-wider ${
                  isActive ? "text-[#e8edf7]" : INK.mute
                }`
              }
            >
              <item.icon className="h-[1rem] w-[1rem]" />
              {item.label}
            </NavLink>
          ))}
        </nav>
        <main className="min-h-0 flex-1 overflow-y-auto px-[2vw] py-[2vh]">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
