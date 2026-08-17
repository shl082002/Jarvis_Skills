import { Navigate, Route, Routes } from "react-router-dom";
import { Shell } from "./components/Shell";
import { BoardPage } from "./pages/BoardPage";
import { RunsPage } from "./pages/RunsPage";
import { ServicesPage } from "./pages/ServicesPage";
import { useCockpit } from "./useCockpit";

export function App() {
  const state = useCockpit();
  if (!state) {
    return (
      <div className="flex h-[100dvh] w-[100vw] items-center justify-center bg-[#0b0e14] text-[0.9rem] text-[#8b95a8]">
        Connecting to the board…
      </div>
    );
  }
  return (
    <Routes>
      <Route element={<Shell state={state} />}>
        <Route index element={<BoardPage state={state} />} />
        <Route path="runs" element={<RunsPage state={state} />} />
        <Route path="services" element={<ServicesPage state={state} />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}
