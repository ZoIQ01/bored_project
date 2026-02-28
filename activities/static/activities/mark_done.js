(() => {
  const STORAGE_KEY = "boredActivities.doneIds.v1";

  function loadDoneIds() {
    try {
      const raw = window.localStorage.getItem(STORAGE_KEY);
      if (!raw) return new Set();
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return new Set();
      return new Set(parsed.map(String));
    } catch {
      return new Set();
    }
  }

  function saveDoneIds(doneIds) {
    const arr = Array.from(doneIds);
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(arr));
  }

  function setRowDoneState(row, isDone) {
    if (!row) return;
    row.classList.toggle("text-decoration-line-through", isDone);
    row.classList.toggle("text-muted", isDone);
    const badge = row.querySelector("[data-activity-done-badge]");
    if (badge) badge.classList.toggle("d-none", !isDone);
  }

  function updateDoneCount(doneIds) {
    const el = document.getElementById("done-count");
    if (!el) return;
    el.textContent = `Done: ${doneIds.size}`;
  }

  function init() {
    const doneIds = loadDoneIds();

    const toggles = document.querySelectorAll("[data-activity-done-toggle]");
    toggles.forEach((toggle) => {
      const activityId = toggle.getAttribute("data-activity-id");
      if (!activityId) return;

      const isDone = doneIds.has(String(activityId));
      toggle.checked = isDone;
      setRowDoneState(toggle.closest("tr"), isDone);

      toggle.addEventListener("change", () => {
        const checked = toggle.checked;
        const key = String(activityId);

        if (checked) doneIds.add(key);
        else doneIds.delete(key);

        saveDoneIds(doneIds);
        setRowDoneState(toggle.closest("tr"), checked);
        updateDoneCount(doneIds);
      });
    });

    const clearBtn = document.getElementById("done-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        doneIds.clear();
        saveDoneIds(doneIds);

        toggles.forEach((toggle) => {
          toggle.checked = false;
          setRowDoneState(toggle.closest("tr"), false);
        });

        updateDoneCount(doneIds);
      });
    }

    updateDoneCount(doneIds);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
